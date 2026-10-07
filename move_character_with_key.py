"""방향키로 소년을 움직이는 Drill 9 실행 파일."""
from time import perf_counter
import pico2d as p
from assets import load_assets
from character import Character
from controls import Controls
from rendering import draw_character
from settings import WIDTH, HEIGHT

def main():
    p.open_canvas(WIDTH, HEIGHT)
    ground, sheet = load_assets(p)
    character = Character()
    controls = Controls()
    keys = {p.SDLK_LEFT: 'left', p.SDLK_RIGHT: 'right',
            p.SDLK_UP: 'up', p.SDLK_DOWN: 'down'}
    running = True
    previous_time = perf_counter()
    while running:
        now = perf_counter()
        dt = min(now - previous_time, 0.1)
        previous_time = now
        for event in p.get_events():
            if event.type == p.SDL_QUIT or (
                event.type == p.SDL_KEYDOWN and event.key == p.SDLK_ESCAPE
            ):
                running = False
            elif (event.type == p.SDL_WINDOWEVENT and
                  event.event == p.SDL_WINDOWEVENT_FOCUS_LOST):
                controls.clear()
            elif event.type == p.SDL_KEYDOWN:
                controls.press(keys.get(event.key))
            elif event.type == p.SDL_KEYUP:
                controls.release(keys.get(event.key))
        if not running:
            break
        character.update(*controls.direction, dt)
        p.clear_canvas()
        ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        draw_character(sheet, character)
        p.update_canvas()
        p.delay(0.01)
    p.close_canvas()

if __name__ == '__main__':
    main()

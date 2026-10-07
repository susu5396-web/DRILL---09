"""방향키로 소년을 움직이는 Drill 9 실행 파일."""
import pico2d as p
from assets import load_assets
from settings import WIDTH, HEIGHT

def main():
    p.open_canvas(WIDTH, HEIGHT)
    ground, sheet = load_assets(p)
    running = True
    while running:
        for event in p.get_events():
            if event.type == p.SDL_QUIT or (
                event.type == p.SDL_KEYDOWN and event.key == p.SDLK_ESCAPE
            ):
                running = False
        p.clear_canvas()
        ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        p.update_canvas()
        p.delay(0.01)
    p.close_canvas()

if __name__ == '__main__':
    main()

"""실제 SDL 창에서 모든 스프라이트를 출력하고 자동 종료한다."""
import pico2d as p
from assets import load_assets
from character import Character
from rendering import draw_character
from settings import WIDTH, HEIGHT


def main():
    p.open_canvas(WIDTH, HEIGHT)
    try:
        ground, sheet = load_assets(p)
        assert (sheet.w, sheet.h) == (802, 402)
        for moving in (False, True):
            for facing in (-1, 1):
                for frame in range(8):
                    p.get_events()
                    p.clear_canvas()
                    ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
                    draw_character(sheet, Character(moving=moving, facing=facing, frame=frame))
                    p.update_canvas()
        print('PASS: image loading and 32 sprite frames')
    finally:
        p.close_canvas()


if __name__ == '__main__':
    main()

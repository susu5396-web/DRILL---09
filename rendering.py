"""스프라이트 시트는 아래부터 좌이동·우이동·좌대기·우대기 순서."""
from settings import FRAME_SIZE

def draw_character(sheet, character):
    row = 3 if character.facing == 1 else 2
    sheet.clip_draw(character.frame * FRAME_SIZE, row * FRAME_SIZE,
                    FRAME_SIZE, FRAME_SIZE, character.x, character.y)

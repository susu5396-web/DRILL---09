"""실행 위치와 무관하게 프로젝트 리소스를 불러온다."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_assets(api):
    names = ('TUK_GROUND.png', 'animation_sheet.png')
    for name in names:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(f'필수 이미지가 없습니다: {ROOT / name}')
    return tuple(api.load_image(str(ROOT / name)) for name in names)

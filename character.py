"""그래픽 라이브러리에 의존하지 않는 캐릭터 상태."""
from dataclasses import dataclass
from settings import WIDTH, HEIGHT, FRAME_SIZE, FRAME_COUNT, SPEED, ANIMATION_FPS

@dataclass
class Character:
    x: float = WIDTH / 2
    y: float = HEIGHT / 2
    facing: int = 1
    moving: bool = False
    frame: int = 0

    def update(self, dx, dy, dt):
        self.x += dx * SPEED * dt
        self.y += dy * SPEED * dt

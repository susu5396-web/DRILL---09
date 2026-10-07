"""그래픽 라이브러리에 의존하지 않는 캐릭터 상태."""
from dataclasses import dataclass
from math import hypot
from settings import WIDTH, HEIGHT, FRAME_SIZE, FRAME_COUNT, SPEED, ANIMATION_FPS

@dataclass
class Character:
    x: float = WIDTH / 2
    y: float = HEIGHT / 2
    facing: int = 1
    moving: bool = False
    frame: int = 0

    def update(self, dx, dy, dt):
        length = hypot(dx, dy)
        if length:
            dx, dy = dx / length, dy / length
        if dx:
            self.facing = 1 if dx > 0 else -1
        self.x += dx * SPEED * dt
        self.y += dy * SPEED * dt
        half = FRAME_SIZE / 2
        self.x = max(half, min(WIDTH - half, self.x))
        self.y = max(half, min(HEIGHT - half, self.y))

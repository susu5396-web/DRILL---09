"""반복 키 이벤트에도 중복되지 않는 방향키 상태."""
class Controls:
    def __init__(self):
        self.pressed = set()

    def press(self, key):
        if key in ('left', 'right', 'up', 'down'):
            self.pressed.add(key)

    def release(self, key):
        self.pressed.discard(key)

    def clear(self):
        self.pressed.clear()

    @property
    def direction(self):
        return (int('right' in self.pressed) - int('left' in self.pressed),
                int('up' in self.pressed) - int('down' in self.pressed))

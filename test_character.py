import unittest
from math import hypot
from character import Character
from controls import Controls
from settings import WIDTH, HEIGHT, SPEED, FRAME_SIZE

class MovementTests(unittest.TestCase):
    def test_four_directions(self):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            with self.subTest(dx=dx, dy=dy):
                c = Character()
                c.update(dx, dy, 0.1)
                self.assertAlmostEqual(c.x, WIDTH / 2 + dx * SPEED * 0.1)
                self.assertAlmostEqual(c.y, HEIGHT / 2 + dy * SPEED * 0.1)

    def test_diagonal_speed(self):
        c = Character()
        c.update(1, 1, 0.1)
        self.assertAlmostEqual(hypot(c.x - WIDTH / 2, c.y - HEIGHT / 2), SPEED * 0.1)

    def test_all_boundaries_and_return(self):
        half = FRAME_SIZE / 2
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)):
            with self.subTest(dx=dx, dy=dy):
                c = Character()
                c.update(dx, dy, 100)
                self.assertTrue(half <= c.x <= WIDTH - half)
                self.assertTrue(half <= c.y <= HEIGHT - half)
                position = c.x, c.y
                c.update(dx, dy, 1)
                self.assertEqual(position, (c.x, c.y))
                self.assertFalse(c.moving)
                c.update(-dx, -dy, 0.1)
                self.assertNotEqual(position, (c.x, c.y))

    def test_vertical_and_idle_preserve_facing(self):
        c = Character()
        for direction in (-1, 1):
            c.update(direction, 0, 0.1)
            for dy in (1, -1, 0):
                c.update(0, dy, 0.1)
                self.assertEqual(c.facing, direction)

    def test_repeat_opposites_and_release(self):
        keys = Controls()
        keys.press('left')
        keys.press('left')
        self.assertEqual(keys.direction, (-1, 0))
        keys.press('right')
        self.assertEqual(keys.direction, (0, 0))
        keys.release('left')
        keys.release('left')
        self.assertEqual(keys.direction, (1, 0))
        keys.clear()
        self.assertEqual(keys.direction, (0, 0))

if __name__ == '__main__':
    unittest.main()

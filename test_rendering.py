import unittest
from unittest.mock import Mock, patch
from types import SimpleNamespace
from character import Character
from rendering import draw_character
from assets import load_assets, ROOT
import move_character_with_key as game

class AnimationTests(unittest.TestCase):
    def test_idle_and_run_wrap(self):
        for moving in (False, True):
            c = Character(moving=moving)
            for _ in range(16):
                c.update(int(moving), 0, 0.05)
            self.assertEqual(c.frame, 0)

    def test_state_changes_reset_frame(self):
        c = Character()
        c.update(0, 0, 0.3)
        self.assertEqual(c.frame, 3)
        c.update(-1, 0, 0.1)
        self.assertEqual(c.frame, 0)
        c.update(0, 0, 0.1)
        self.assertEqual(c.frame, 0)

    def test_all_sprite_rows(self):
        for moving, facing, row in ((True, -1, 0), (True, 1, 1),
                                    (False, -1, 2), (False, 1, 3)):
            sheet = Mock()
            c = Character(moving=moving, facing=facing, frame=7)
            draw_character(sheet, c)
            sheet.clip_draw.assert_called_once_with(700, row * 100, 100, 100, c.x, c.y)

    def test_absolute_asset_paths(self):
        api = Mock()
        load_assets(api)
        self.assertEqual(api.load_image.call_args_list[0].args, (str(ROOT / 'TUK_GROUND.png'),))

    def test_exit_and_error_close_canvas(self):
        for kind in ('quit', 'escape', 'error'):
            api = Mock()
            api.SDL_QUIT = 1
            api.SDL_KEYDOWN = 2
            api.SDLK_ESCAPE = 27
            api.get_events.return_value = [SimpleNamespace(type=1 if kind == 'quit' else 2, key=27)]
            with patch.object(game, 'p', api), patch.object(game, 'load_assets') as assets:
                assets.return_value = (Mock(), Mock())
                if kind == 'error':
                    assets.side_effect = RuntimeError('load failure')
                    with self.assertRaises(RuntimeError):
                        game.main()
                else:
                    game.main()
                api.close_canvas.assert_called_once()

    def test_focus_loss_clears_input_before_update(self):
        api = Mock()
        api.SDL_QUIT, api.SDL_KEYDOWN, api.SDL_KEYUP = 1, 2, 3
        api.SDLK_ESCAPE, api.SDLK_RIGHT = 27, 100
        api.SDL_GetKeyboardFocus.return_value = None
        api.get_events.side_effect = [
            [SimpleNamespace(type=2, key=100)],
            [SimpleNamespace(type=1)],
        ]
        with patch.object(game, 'p', api), patch.object(game, 'load_assets', return_value=(Mock(), Mock())), patch.object(game, 'Character') as cls:
            game.main()
            self.assertEqual(cls.return_value.update.call_args.args[:2], (0, 0))
            api.close_canvas.assert_called_once()

if __name__ == '__main__':
    unittest.main()

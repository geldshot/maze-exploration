import unittest
from maze.window import Window

class TestWindow(unittest.TestCase):
    window = None
    
    def test_window_creation(self):
        self.window = Window(600, 800)
        self.window.wait_for_close()
        self.assertTrue(self.window.running)

    def tearDown(self):
        if self.window:
            self.window.close()
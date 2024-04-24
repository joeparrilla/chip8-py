from pygame import display

DISPLAY_HEIGHT = 32
DISPLAY_WIDTH = 64

class Display:
    def __init__(self):
        self.screen = [ [0] * DISPLAY_WIDTH for _ in range(DISPLAY_HEIGHT)]

    def dump_screen_bits(self):
        for i in range(DISPLAY_HEIGHT):
            print(self.screen[i])
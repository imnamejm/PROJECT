from pico2d import *
import random
import game_framework

class Retry:
    def __init__(self):
        self.image = load_image('retry.png')
        self.score = 0
        self.x = 600
        self.y = 400
        self.TFdraw = False

    def update(self):
        pass
    def draw(self):
        if self.TFdraw:
            self.image.draw(self.x, self.y)

    def do_drawing(self):
        self.TFdraw = True

    def not_drawing(self):
        self.TFdraw = False
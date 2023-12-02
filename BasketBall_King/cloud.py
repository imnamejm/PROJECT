from pico2d import *
import game_framework

class Cloud:
    def __init__(self):
        self.image = load_image('cloud2.png')
        self.score = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 750)

    def score_load(self, score):
        self.score = score

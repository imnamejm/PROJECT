from pico2d import *
import random
import game_framework

class Cloud:
    def __init__(self):
        self.image = load_image('cloud3.png')
        self.score = 0
        self.x = random.randint(100, 1100)
        self.y = random.randint(400, 700)
        self.velocity = 1

    def update(self):
        if self.x > 950:
            self.velocity = -1
        elif self.x < 150:
            self.velocity = 1
        self.x += self.velocity * 100 * game_framework.frame_time
    def draw(self):
        if self.score >= 60:
            self.image.draw(self.x, self.y)

    def score_load(self, score):
        self.score = score

from pico2d import *
import random
import game_framework

class Bird:
    def __init__(self):
        self.image = load_image('bird.png')
        self.score = 0
        self.x = random.randint(100, 1100)
        self.y = random.randint(400, 700)
        self.velocity = -1

    def update(self):
        if self.x < 0:
            self.x = 1100
            self.y = random.randint(400, 700)
        self.x += self.velocity * 100 * game_framework.frame_time

    def draw(self):
        if 60 > self.score >= 30:
            self.image.draw(self.x, self.y)

    def score_load(self, score):
        self.score = score

    def init(self):
        self.score = 0
        self.x = random.randint(100, 1100)
        self.y = random.randint(400, 700)
        self.velocity = -1

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 30

    def stop(self):
        self.velocity = 0
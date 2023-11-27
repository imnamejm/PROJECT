from pico2d import *
import game_world
import game_framework
from ball import Ball

class Ring:
    def __init__(self, x = 600, y = 475, pattern = 0, velocity = 1):
        self.image = load_image('target2.png')
        self.x, self.y, self.pattern, self.velocity = x, y, pattern, velocity
        self.score = 0

    def change_pattern(self):
        if 0 <= self.score < 10:
            self.pattern = 0
            self.velocity = 0
        elif 10 <= self.score < 20:
            self.pattern = 1
            self.velocity = 1
        elif 20 <= self.score < 30:
            self.pattern = 2
            self.velocity = 1

    def update(self):
        self.change_pattern()

        if self.pattern == 0:
            self.x = 600
            self.y = 475

        elif self.pattern == 1:
            print("a")
            if self.x > 750:
                self.velocity = -1
            elif self.x < 450:
                self.velocity = 1
            self.x += self.velocity * 50 * game_framework.frame_time

        elif self.pattern == 2:
            if self.y > 525:
                self.velocity = -1
            elif self.y < 425:
                self.velocity = 1
            self.y += self.velocity * 50 * game_framework.frame_time

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 103, self.y - 8, self.x + 103, self.y + 8

    def get_lc_point(self):
        return self.x - 103, self.y

    def get_rc_point(self):
        return self.x + 103, self.y

    def stop(self):
        self.pattern = 0

    def score_plus(self):
        self.score += 1


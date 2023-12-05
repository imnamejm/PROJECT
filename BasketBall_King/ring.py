from pico2d import *
import game_world
import game_framework
from ball import Ball

class Ring:
    def __init__(self, x = 600, y = 475, pattern = 0, velocity = 1):
        self.image = load_image('target2.png')
        self.x, self.y, self.pattern, self.velocity = x, y, pattern, velocity
        self.score = 0
        self.ball = 0

    def init(self):
        self.image = load_image('target2.png')
        self.x, self.y, self.pattern, self.velocity = 600, 475, 0, 1
        self.score = 0
        self.ball = 0

    def change_pattern(self):
        if 0 <= self.score < 10:
            self.pattern = 0
        elif 10 <= self.score < 20:
            self.pattern = 1
        elif 20 <= self.score < 30:
            self.pattern = 2
        elif 30 <= self.score < 40:
            self.pattern = 0
        elif 40 <= self.score < 50:
            self.pattern = 1
        elif 50 <= self.score < 60:
            self.pattern = 2
        elif 60 <= self.score < 70:
            self.pattern = 0
        elif 70 <= self.score < 80:
            self.pattern = 1
        elif 80 <= self.score < 90:
            self.pattern = 2


    def update(self):
        self.change_pattern()

        if self.pattern == 0:
            self.x = 600
            self.y = 475

        elif self.pattern == 1:
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
        if self.ball == 2:
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 103, self.y - 8, self.x + 103, self.y + 8

    def get_lc_point(self):
        return self.x - 103, self.y

    def get_rc_point(self):
        return self.x + 103, self.y

    def stop(self):
        self.pattern = 0

    def score_load(self, score):
        self.score = score

    def get_ball(self, ball_state):
        self.ball = ball_state

from pico2d import *

class Field:
    def __init__(self):
        self.score = 0
        self.background_type = 1
        self.image1 = load_image('field.png')
        self.image2 = load_image('mountain.png')
        self.image3 = load_image('sky.png')
        self.clear_image = load_image('clear.png')

    def update(self):
        pass

    def draw(self):
        if 0 <= self.score < 30:
            self.image1.draw(600, 400)
        elif 30 <= self.score < 60:
            self.image2.draw(600, 400)
        elif 60 <= self.score < 90:
            self.image3.draw(600, 400)
        elif self.score >= 90:
            self.clear_image.draw(600, 400)


    def score_load(self, score):
        self.score = score

    def cheat(self):
        pass
from pico2d import *
import game_world
import game_framework
from ball import Ball

class Setting:
    def __init__(self):
        self.image = load_image('setting.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1150, 750)

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1050, 750)

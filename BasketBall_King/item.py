from pico2d import *
import game_framework
import game_world

class Item:
    def __init__(self):
        self.image = load_image('item.png')
        self.item = True

    def update(self):
        pass

    def draw(self):
        if self.item:
            self.image.draw(50, 750)

    def use_item(self):
        self.item = False

    def init(self):
        self.item = True
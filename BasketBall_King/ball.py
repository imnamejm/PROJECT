from pico2d import *
import game_framework


def shoot_ball(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].type == SDL_BUTTON_LEFT

Gravity = 9.8

class Ball:
    image = None
    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('basicball.png')
            self.grab = False
            self.shoot = 0
            self.x, self.y, self.velocity = 600, 100, 1  # 1 = UP / -1 =DOWN
            self.prev_x, self.prev_y = 600, 100  # prev_x, prev_y = previous_x, previous_y
            self.d_x = 0
            self.speed = 160
            self.bgm = load_music('Coin 1.mp3')
            self.bgm.set_volume(30)

    def init(self):
        self.grab = False
        self.shoot = 0
        self.x, self.y, self.velocity = 600, 100, 1  # 1 = UP / -1 =DOWN
        self.prev_x, self.prev_y = 600, 100  # prev_x, prev_y = previous_x, previous_y
        self.d_x = 0
        self.speed = 160

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        # 공 이동 제한
        if self.x < 100:
            self.x = 100
        elif self.x > 1100:
            self.x = 1100

        if self.y < 100:
            self.y = 100
            self.velocity = 1
            self.x = 600  # 공이 땅에 닿으면 처음 위치로
            self.shoot = 0

        elif self.y > 700:
            self.y = 700
            self.shoot = 2
            self.speed = 140

        if not self.shoot == -1:
            # 슛
            if 700 > self.y > 400 and not self.grab:
                if self.shoot == 0 or self.shoot == 1:
                    self.shoot = 1
                    self.y += self.speed * Gravity * game_framework.frame_time
                    self.speed -= 50 * Gravity * game_framework.frame_time
                    if self.speed < 0:
                        self.speed = 0
                        self.shoot = 2

            # 중력
            if not self.grab:
                self.y -= Gravity * 70 * game_framework.frame_time

                if not self.d_x == 0:
                    self.x += self.d_x * 100 * game_framework.frame_time

    def handle_event(self, event):
        pass

    def stop(self):
        self.shoot = -1  # 슛 실패 (골대와 충돌)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def get_c_point(self):
        return self.x, self.y

    def put_mouse(self, mx, my):
        self.x = mx
        self.y = my
        self.grab = True

    def save_mouse(self):
        self.grab = False
        self.d_x = self.x - self.prev_x

    def move_mouse(self, mx, my):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x = mx
        self.y = my

    def ball_statement(self):
        return self.shoot

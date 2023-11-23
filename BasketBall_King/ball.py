from pico2d import *
import game_framework
import game_world


def shoot_ball(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].type == SDL_BUTTON_LEFT

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('basicball.png')
            self.state_machine = StateMachine(self)
            self.x, self.y, self.velocity = 600, 100, 1  # 1 = UP / -1 =DOWN
            self.sx, self.sy = 600, 100  # sx, sy = shoot_x, shoot_y

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # 공 이동 제한
        if self.x < 100:
            self.x = 100
        elif self.x > 1100:
            self.x = 1100

        if self.y < 100:
            self.y = 100
        elif self.y > 700:
            self.y = 700

        # 중력
        if self.y < 400:
           self.y -= self.velocity * 100 * game_framework.frame_time

        # 슛
        if 700 > self.y > 400:
            self.y += self.velocity * 1 * game_framework.frame_time
            self.x += (self.sy - 100 / self.sx - 600) * 1 * game_framework.frame_time
            self.velocity = -1

        if self.y <= 700:
            if self.velocity == -1:  # 공이 내려감
                if self.y > 100:
                    self.y += self.velocity * 10 * game_framework.frame_time
                    self.x += (self.sy - 100 / self.sx - 600) * 10 * game_framework.frame_time
                else:
                    self.velocity = 1

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def put_mouse(self, mx, my):
        self.x = mx
        self.y = my

    def save_mouse(self, mx, my):
        self.sx = mx
        self.sy = my

class Idle:
    @staticmethod
    def select(ball, e):
        pass

    @staticmethod
    def shoot(ball, e):
        pass

    @staticmethod
    def stop(ball):
        pass

    @staticmethod
    def draw(ball):
        pass

class Grab:
    @staticmethod
    def select(ball, e):
        pass
    @staticmethod
    def shoot(ball, e):
        pass

    @staticmethod
    def stop(ball):
        pass

    @staticmethod
    def draw(ball):
        pass

class StateMachine:
    def __init__(self, ball):
        pass
#        self.ball = ball
#        self.cur_state = Idle
#        self.transitions = {
#            Idle: {shoot_ball: Grab},
#            Grab: {shoot_ball: Idle}
#        }
    def update(self):
        pass
#        self.cur_state.stop(self.ball)


    def handle_event(self, e):
        pass
#        for check_event, next_state in self.transitions[self.cur_state].items():
#            if check_event(e):
#                self.cur_state.select(self.ball, e)
#                self.cur_state = next_state
#                self.cur_state.shoot(self.ball, e)
#                return True
#        return False

    def draw(self):
        pass
#        self.cur_state.draw(self.ball)

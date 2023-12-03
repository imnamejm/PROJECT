from pico2d import *
import game_framework
import game_world


def shoot_ball(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].type == SDL_BUTTON_LEFT

Gravity = 9.8

class Ball:
    image = None
    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('basicball.png')
            self.state_machine = StateMachine(self)
            self.grab = False
            self.shoot = 0
            self.x, self.y, self.velocity = 600, 100, 1  # 1 = UP / -1 =DOWN
            self.prev_x, self.prev_y = 600, 100  # prev_x, prev_y = previous_x, previous_y
            self.d_x = 0
            self.speed = 160

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

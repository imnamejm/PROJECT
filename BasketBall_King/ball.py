from pico2d import *
import game_framework
import game_world

def pick_ball(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].type == SDL_BUTTON_LEFT

def shoot_ball(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].type == SDL_BUTTON_LEFT

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('basicball.png')
            self.state_machine = StateMachine(self)
            self.x, self.y, self.velocity = 600, 100, 1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_event(self, event):
       pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def put_mouse(self, x, y):
        self.x = x
        self.y = y


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
#            Idle: {pick_ball: Grab, shoot_ball: Grab},
#            Grab: {pick_ball: Idle, shoot_ball: Idle}
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

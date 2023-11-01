# 이것은 각 상태들을 객체로 구현한 것임.
from random import randrange

from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# bird Run Speed
# fill here
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


# bird Action Speed
# fill here
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION










class Idle:

    @staticmethod
    def enter(bird, e):
        bird.dir = 0
        bird.frame = 0
        bird.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        # bird.frame = (bird.frame + 1) % 8
        bird.frame = (bird.frame + FRAMES_PER_TIME * game_framework.frame_time) % 14

    @staticmethod
    def draw(bird):
        if bird.face_dir == 1:
            bird.image.clip_draw(int(bird.frame) % 5 * 183, int(2 - int(int(bird.frame) / 5)) * 168, 181, 168, bird.x, bird.y,
                                 92, 84)
        elif bird.face_dir == -1:
            bird.image.clip_composite_draw(int(bird.frame) % 5 * 183, int(2 - int(int(bird.frame) / 5)) * 168, 181, 168, 0, 'h', bird.x, bird.y,
                                 92, 84)



class Run:

    @staticmethod
    def enter(bird, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            bird.dir, bird.face_dir = 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            bird.dir, bird.face_dir = -1, -1

    @staticmethod
    def exit(bird, e):
        if space_down(e):
            bird.fire_ball()

        pass

    @staticmethod
    def do(bird):
        # bird.frame = (bird.frame + 1) % 5
        bird.frame = (bird.frame + FRAMES_PER_TIME * game_framework.frame_time)
        if bird.frame > 14:
            bird.frame = 0
        # bird.x += bird.dir * 5
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600-25)


    @staticmethod
    def draw(bird):
        if bird.face_dir == 1:
            bird.image.clip_draw(int(bird.frame) % 5 * 183, int(2 - int(int(bird.frame) / 5)) * 168, 181, 168, bird.x,
                                 bird.y,
                                 92, 84)
        elif bird.face_dir == -1:
            bird.image.clip_composite_draw(int(bird.frame) % 5 * 183, int(2 - int(int(bird.frame) / 5)) * 168, 181, 168,
                                           0, 'h', bird.x, bird.y,
                                           92, 84)


class StateMachine:
    def __init__(self, bird):
        self.bird = bird
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
        }

    def start(self):
        self.cur_state.enter(self.bird, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.bird)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.bird, e)
                self.cur_state = next_state
                self.cur_state.enter(self.bird, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.bird)





class Bird:
    def __init__(self):
        self.x, self.y = randrange(0, 1000), 300
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = 'Ball'
        self.font = load_font('ENCR10B.TTF', 16)


    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))
        print(int(self.frame) % 5, int(2 - int(int(self.frame)) / 5))

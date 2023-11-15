from pico2d import *


# player가 사용하는 기본 chatecter인 Bike이다.
# Bike의 StateMachine을 받아서 처리 할 수 있어야 된다.

# 키 입력 이벤트
def keyboard_right_down(e):      #오른쪽 키 누름
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
def keyboard_right_up(e):        #오른쪽 키 땜
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
def keyboard_left_down(e):       # 왼쪽 키 누름
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
def keyboard_left_up(e):         #왼쪽 키 땜
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
def keyboard_up_up(e):           #위쪽 키 누름
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
def keyboard_up_down(e):         #위쪽 키 땜
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def keyboard_down_up(e):         #아래쪽 키 누름
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN
def keyboard_down_down(e):       #아래쪽 키 땜
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
def space_down(e):               #스페이스바 누름
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

class StateMachine: # bike의 StateMachine
    def __init__(self, bike):
        self.bike = bike
        self.cur_state = Idle
        self.transitions = {} # 각 상태 확인 튜플형식으로 진행할 것

    def start(self):
        self.cur_state.enter(self.bike, ('NONE', 0)) #시작시 진행

    def update(self):
        self.cur_state.do(self.bike)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.bike, e)
                self.cur_state = next_state
                self.cur_state.enter(self.bike, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.bike)


class Bike:
    def __init__(self):
        self.x, self.y = 136, 133 #bike의 x,y Size
        self.frame = 0
        self.action = 6 # 6이 idle상태
        self.dir = 0
        self.image = load_image('bike_move_motion.png')
        self.state_machine = StateMachine(self)

    def update(self):
        self.frame = (self.frame + 1) % 3

    def handle_event(self, event):
        print(event) # 이벤트 발생하는지 확인하기 위해 사용
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 136,0,136,128,100,400)
        # self, left, bottom, width, height, x, y, w, h

#자전거 함정
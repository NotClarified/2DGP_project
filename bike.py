from pico2d import *


# player가 사용하는 기본 chatecter인 Bike이다.
# Bike의 StateMachine을 받아서 처리 할 수 있어야 된다.
class Bike:
    def __init__(self):
        self.x, self.y = 136, 133 #bike의 x,y Size
        self.frame = 0
        self.action = 6 # 6이 idle상태
        self.dir = 0
        self.image = load_image('bike_move_motion.png')

    def update(self):
        self.frame = (self.frame + 1) % 3

    def handle_event(self, event):
        print(event) # 이벤트 발생하는지 확인하기 위해 사용
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 136,0,136,128,100,400)
        # self, left, bottom, width, height, x, y, w, h
def reset_world():
    global running
    global bike
    global world

    running = True
    world = []

    bike = Bike() #bike 객체 변수
    world.append(bike)

def update_world():
    for o in world: # o == object
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()
reset_world()

while running:
    update_world()
    render_world()
    delay(1)

close_canvas()

#자전거 함정
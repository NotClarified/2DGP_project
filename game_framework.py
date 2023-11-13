# 교수님 수업 자료 참고하여 진행하였습니다.

import time


def change_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].finish()
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if (len(stack) > 0):
        stack[-1].finish()
        stack.pop()

    if (len(stack) > 0):
        stack[-1].resume()


def quit():                                                             # game 종료
    global running
    running = False

# start mode
def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

    global frame_time                                                   # frame_time을 통해 성능에 상관없이 정형화 시킬 수 있다.
    frame_time = 0.0                                                    # frame_time init
    current_time = time.time()
    while running:
        stack[-1].handle_events()                                       # handle_events받기
        stack[-1].update()                                              # update받기
        stack[-1].draw()                                                # draw받기
        frame_time = time.time() - current_time                         # 진행시간 frame_time으로 받기
        frame_rate = 1.0 / frame_time                                   # frame_rate 받기
        current_time += frame_time                                      # 진행시간 추가
        #print(f'Frame Time: {frame_time}, Frame Rate: {frame_rate}')   # 얼마나 진행되었는지 확인하기위한 코드

    # 종료 후 모든 스택 pop하기
    while (len(stack) > 0):
        stack[-1].finish()
        stack.pop()

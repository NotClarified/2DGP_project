objects = [[] for _ in range(3)] #레이어 3개

collision_pairs = {}            # 각 충돌 처리
def add_object(o, depth = 0):   # object추가시 해당하는 레이어에 추가
    objects[depth].append(o)

def add_objects(ol, depth = 0): # objectlist 추가시 해당하는 레이어에 추가, 여러개 장해물 동시에 넣기
    objects[depth] += ol


def update():                   # update시 오브젝트 전체 상태 update진행
    for layer in objects:
        for o in layer:
            o.update()


def render():                   # render시 오브젝트 전체 그리기
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):           # 오브젝트 삭제하기 레이어 확인하고 삭제
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')


def clear():                    # 화면 클리어하기
    for layer in objects:
        layer.clear()

def collide(a, b):              # 충돌 범위 체크
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

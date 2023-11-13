objects = [[] for _ in range(3)] #레이어 3개

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
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():                    # 화면 클리어하기
    for layer in objects:
        layer.clear()
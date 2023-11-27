objects = [[] for _ in range(4)]

collision_pairs = {}

def add_collision_pair(group, a, b):
   pass

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol

def update():
    for layer in objects:
        for o in layer:
            o.update()

def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_collision_object(o):
    pass

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()

def handle_collisions():
    pass

def ring_ball_col(a, b):  # 골대 충돌 일어났는지
    ball_x, ball_y = a.get_c_point()
    ring_lx, ring_ly = b.get_lc_point()
    ring_rx, ring_ry = b.get_rc_point()

    left_d = (ball_x - ring_lx)**2 + (ball_y - ring_ly)**2
    right_d = (ball_x - ring_rx)**2 + (ball_y - ring_ry)**2

    if left_d <= 250 or right_d <= 250:
        return True

    return False

def goal(a, b):  # 골인 했는지
    ball_x, ball_y = a.get_c_point()
    ring_lx, ring_ly = b.get_lc_point()
    ring_rx, ring_ry = b.get_rc_point()

    if ball_x > ring_lx and ball_x < ring_rx:
        if abs(ball_y - ring_ly) < 0.5:
            return True

    return False

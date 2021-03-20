import math

def vector_rotation(x, y, th, f = 1.0):
    th = -th * math.pi / 180.0
    rx = x * math.cos(th) - y * math.sin(th)
    ry = x * math.sin(th) + y * math.cos(th)
    return (rx * f, ry * f)
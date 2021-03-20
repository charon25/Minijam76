import math
import pygame as pyg

def vector_rotation(x, y, th, f = 1.0):
    th = -th * math.pi / 180.0
    rx = x * math.cos(th) - y * math.sin(th)
    ry = x * math.sin(th) + y * math.cos(th)
    return (rx * f, ry * f)

def distance(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

def polar_to_cartesian(r, angle):
    return (r * math.cos(angle), r * math.sin(angle))
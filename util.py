import math
import co
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

def is_point_in_rect(rect : pyg.Rect, x, y):
    return rect.left <=x <= rect.right and rect.top <= y <= rect.bottom

def get_font(size):
    try:
        return pyg.font.Font(co.FONT_PATH, size)
    except:
        return pyg.font.SysFont("arial", size)
    
def draw_text(screen, text, size, pos, color):
    font = get_font(size)
    img = font.render(text, False, color)
    screen.blit(img, pos)
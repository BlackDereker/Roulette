import pygame
import math
import random
from colorsys import rgb_to_hsv, hsv_to_rgb

def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return (r, g, b)

def complementary_color(color):
    hsv = rgb_to_hsv(color[0], color[1], color[2])
    return hsv_to_rgb(((hsv[0] + 0.5) % 1), hsv[1], hsv[2])

def draw_partial_circle(surface, color, pos, radius, start_angle, final_angle):
    global first
    points = [pos]
    for i in range(start_angle, final_angle + 1):
        x = pos[0] + int(math.cos(math.radians(i)) * radius)
        y = pos[1] + int(math.sin(math.radians(i)) * radius)
        points.append((x, y))
    points.append(pos)
    pygame.draw.polygon(surface, color, points)

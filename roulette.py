import pygame
from draw_utils import draw_partial_circle
from draw_utils import random_color
from draw_utils import complementary_color

class Roulette:
    
    angle_offset = 0
    
    def generate_colors(self):
        colors = []
        for i in range(len(self._topics)):
            if i == 0:
                colors.append(random_color())
            elif i == len(self._topics) - 1 and i % 2 == 0:
                colors.append(random_color())
            else:
                colors.append(complementary_color(colors[i-1]))
        self._colors = colors
    def rotate(self, angle):
        self.angle_offset += angle
    def draw(self, surface, pos):
        topic_angle = 360 // len(self._topics)
        angle = self.angle_offset
        for i in range(len(self._topics)):
            draw_partial_circle(surface, self._colors[i], pos, self._size, angle, angle + topic_angle)
            angle += topic_angle
    def __init__(self, size, topics):
        self._topics = topics
        self._size = size
        self.generate_colors()

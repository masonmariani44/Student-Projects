import pygame
from pygame import Rect

class Level:

    def __init__(self):
        self.solid_ground = [Rect(50, 300, 500, 50)]

    def draw(self, screen):
        for obj in self.solid_ground:
            pygame.draw.rect(screen, (0, 255, 0), obj)
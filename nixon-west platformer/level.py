import pygame
from pygame import Rect

class Level:

    def __init__(self):
        self.platforms = [
            
            Rect(50, 300, 500, 50),
            Rect(100, 200, 50, 100)

            ]


    def get_platforms(self):
        return self.platforms

    
    def draw(self, screen):

        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)

        
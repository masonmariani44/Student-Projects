import pygame
from pygame import Rect, Vector2

class Player:

    def __init__(self):
        self.rect = Rect(50, 50, 25, 25)

    def handle_events(self, all_events):

        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("pressed d")

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
    
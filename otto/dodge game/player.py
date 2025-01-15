import pygame
from pygame import Rect, Vector2

WIDTH = 50
HEIGHT = 50

PLAYER_SPEED = 12

white = (255, 255, 255)

key_pressed = {"left" : False, "right" : False}

class Player:
    def __init__(self):

        self.rect = pygame.Rect(0, 0, 50, 50)
        self.point = 1

    
    def update(self, all_events):
        
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    key_pressed["right"] = True
                if event.key == pygame.K_a:
                    key_pressed["left"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    key_pressed["right"] = False
                if event.key == pygame.K_a:
                    key_pressed["left"] = False

        # actually move our character
        if key_pressed["right"]:
            self.rect.center = Vector2(self.rect.center) + Vector2(PLAYER_SPEED, 0)
        if key_pressed["left"]:
            self.rect.center = Vector2(self.rect.center) + Vector2(-PLAYER_SPEED, 0)



    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
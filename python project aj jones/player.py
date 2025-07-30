import pygame
from pygame import Rect, Vector2

class Player:

    def __init__(self):
        self.rect = Rect(50, 50, 50, 50)
        self.keys_pressed = {"left" : False, "right" : False}
        

    def handle_events(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.keys_pressed["right"] = True
                if event.key == pygame.K_a:
                    self.keys_pressed["left"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.keys_pressed["right"] = False
                if event.key == pygame.K_a:
                    self.keys_pressed["left"] = False
    

    def update(self):
        


    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
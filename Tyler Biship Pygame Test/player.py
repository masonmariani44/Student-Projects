import pygame
from pygame import Rect, Vector2

class Player:

    def __init__(self):

        self.key_pressed = { 
                            "up":False,     #w
                            "down":False,   #s
                            "right":False,  #d
                            "left":False    #a
                            }

        self.rect = Rect(5, 5, 30, 30)

        self.x_pos = self.rect.centerx
        self.y_pos = self.rect.centery

        self.velocity = Vector2(0, 0)

    def update(self, all_events):
        
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.key_pressed["up"] = True
                if event.key == pygame.K_s:
                    self.key_pressed["down"] = True
                if event.key == pygame.K_a:
                    self.key_pressed["left"] = True
                if event.key == pygame.K_d:
                    self.key_pressed["right"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.key_pressed["up"] = False
                if event.key == pygame.K_s:
                    self.key_pressed["down"] = False
                if event.key == pygame.K_a:
                    self.key_pressed["left"] = False
                if event.key == pygame.K_d:
                    self.key_pressed["right"] = False
        

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
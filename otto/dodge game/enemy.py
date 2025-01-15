import pygame
import random 

class Enemy():

    def __init__(self):
        img_width = 50
        # randomize position 
        random_x_pos = random.randint(0, img_width+1)

        self.rect = pygame.Rect(random_x_pos, 0, img_width, img_width)

        self.is_alive = True
    
    def update():
        return 
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
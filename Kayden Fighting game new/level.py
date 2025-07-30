import pygame
from pygame import Rect

class Level:
    def __init__(self):
        self.platforms = [Rect(50, 300, 500, 50)]
        #self.platforms = []
        return


    def draw(self, screen):
        for platform in self.platforms:


            #TODO this is not done lol
            player_image = pygame.transform.scale(self.image, self.rect.size)
            player_image.convert()

            surface.blit(player_image, self.rect)
            screen.blit(surface, (0, 0))



            pygame.draw.rect(screen, (0,255,0), platform)
            
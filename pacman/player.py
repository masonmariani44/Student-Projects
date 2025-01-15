import pygame, os

class Player:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),"assets", "Barry Blue Py.png.png"))
        self.rect = self.image.get_rect()

        image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(image_size[0]*.1), int(image_size[1]*.1)))

        self.rect = self.image.get_rect()


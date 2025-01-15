import pygame, sys, os 
from pygame.locals import QUIT

from player import Player

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("PIE MAN: THE 1ST BATCH")


player = Player()

while True:
    events = pygame.event.get()
    screen.fill((185, 233, 237))

    screen.blit(player.image, player.rect)

    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(30, 30, 50, 50))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (50, 50), 20)

    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()
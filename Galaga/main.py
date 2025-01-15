from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
from pygame.locals import *
from sys import exit

import player

pygame.init()

#player stuff
player_image = pygame.image.load("sprites/player.png")
player_rect = player_image.get_rect()

size = player_image.get_size()
player_image = pygame.transform.scale(player_image, (int(size[0]*.5), int(size[1]*.5)))

#screen 
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Galaga")

clock = pygame.time.Clock()
FPS = 30

player = player.Player()

def main():
    while True:
        handle_events()
        update()
        draw()

def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


def update():
    clock.tick(FPS)

def draw():
    
    screen.fill((0, 0, 0))

    screen.blit(player_image, player_rect)
    pygame.display.flip()

main()

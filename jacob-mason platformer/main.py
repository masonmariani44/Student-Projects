from os import environ
import pygame
from pygame.locals import *
from player import Player

pygame.init()

FPS = 30

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

player = Player()


def handle_events():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == QUIT:
            pygame.quit()
            exit()
    return all_events


def update(all_events):
    player.update(all_events)

def draw():
    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.flip()


def main():
    while True:
        clock.tick(FPS)
        all_events = handle_events()
        update(all_events)
        draw()

main()
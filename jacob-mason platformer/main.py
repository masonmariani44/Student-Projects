from os import environ
import pygame
from pygame.locals import *
from player import Player
from level import Level

pygame.init()

FPS = 30

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

player = Player()
level = Level()


def handle_events():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == QUIT:
            pygame.quit()
            exit()
    return all_events


def update(all_events):
    player.update(all_events)
    handle_collision()

def draw():
    screen.fill((255, 255, 255))
    player.draw(screen)
    level.draw(screen)
    pygame.display.flip()


def handle_collision():
    for platform in level.solid_ground:
        player.on_ground = player.rect.colliderect(platform)
        if player.on_ground:
            difference = platform.topleft[1] - player.rect.bottomright[1]
            player.rect.move_ip(0, difference)




def main():
    while True:
        clock.tick(FPS)
        all_events = handle_events()
        update(all_events)
        draw()

main()
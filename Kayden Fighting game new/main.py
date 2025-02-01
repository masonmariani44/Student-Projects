from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
 
import pygame
from pygame.locals import *
from sys import exit
from level import Level
from player import Player

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Fighting Game")
clock = pygame.time.Clock()

level = Level()
player = Player()

"""

player left/right movement

player jumping

smash bros style attacks
    specials
    normals
    directional 

lose condition

ledge grabbing

solid ground vs platforms

blocking
    parry

dodging

sprites

"""

def main():
    
    while True:
        clock.tick(FPS)
        all_events = handle_events()
        update(all_events)
        draw()
 
def handle_events():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == QUIT:
            pygame.quit()
            exit()
    return all_events
 
def update(all_events):
    player.update(all_events, clock)
    handle_collision()

def draw():
    screen.fill((255,255,255))
    level.draw(screen)
    player.draw(screen)
    pygame.display.flip()

def handle_collision():
    
    for rect in level.platforms:
        player.on_ground = player.rect.colliderect(rect)
        if player.on_ground is True:
            difference = rect.topleft[1] - player.rect.bottomright[1]
            player.rect.move_ip(0, difference)



    
 
main()
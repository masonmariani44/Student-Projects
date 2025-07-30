import pygame
from pygame.locals import *
from sys import exit
from player import Player

pygame.init()

SCREEN_X = 600
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
surface = pygame.Surface(screen.get_size())
pygame.display.set_caption("PacMan Game")
clock = pygame.time.Clock()

my_player = Player(SCREEN_X, SCREEN_Y)

def main():
    while True:
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
    my_player.update(all_events)

def draw():
    screen.fill((255, 255, 255))
    my_player.draw(screen)
    pygame.display.flip()

main()
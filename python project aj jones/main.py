import pygame
from sys import exit
from player import Player

pygame.init()

screen = pygame.display.set_mode((600, 600))

my_player = Player()

def handle_events():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    my_player.handle_events(all_events)

def update():
    pass

def draw():
    screen.fill((255, 255, 255))
    my_player.draw(screen)
    pygame.display.update()

while True:
    handle_events()
    update()
    draw()
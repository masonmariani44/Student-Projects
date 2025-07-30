from os import environ
import pygame
from pygame.locals import *
import pygame_gui
import pygame_gui.ui_manager
from battle_menu import Battle_Menu

pygame.init()

FPS = 30
time_delta = 0

screen_height = 1080
screen_width = 1920
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

background = pygame.Surface((screen_width, screen_height))
background.fill(pygame.Color("#000000"))

manager = pygame_gui.UIManager((screen_width, screen_height))


#hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             #text='Say Hello',
                                            # manager=manager)

my_battle = Battle_Menu(manager, screen_width, screen_height)


def handle_events():
    all_events = pygame.event.get()
    for event in all_events:

        if event.type == QUIT:
            pygame.quit()
            exit()
    
    manager.update(time_delta)

    my_battle.handle_events(all_events)

    return all_events


def update():
    return

def draw():
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)


    pygame.display.update()

def main():
    while True:
        # clock tick stuff
        time_delta = clock.tick(FPS) / 1000.0

        all_events = handle_events()
        update()
        draw()

main()
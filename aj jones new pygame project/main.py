import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 600))



def handle_events():
    
    all_events = pygame.event.get()
    for event in all_events:

        if event != "":
            print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




while True:
    
    handle_events()
    #update()
    #draw()



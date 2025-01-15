from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from sys import exit

from player import Player
from enemy import Enemy

pygame.init()
FPS = 30
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("template")
clock = pygame.time.Clock()

p = Player()
p.rect.x = 250
p.rect.y = 450

enemy = Enemy()



"""

TODO:

make things that fall
  on enemy collision: 
    player loses health & gets squished
  friendly things fall on collision:
    increase score

sprites

"""



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
  p.update(all_events)
  clock.tick(FPS)

def draw():
  screen.fill((0,0,0))
  p.draw(screen)
  enemy.draw(screen)

  pygame.display.flip()

main()
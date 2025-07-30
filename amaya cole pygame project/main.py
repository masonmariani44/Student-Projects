import sys

import pygame
from pygame.locals import *

from player import Player
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  all_events = pygame.event.get()
  for event in all_events:
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    

  
  # Update.
  
  # Draw.
  
  pygame.display.flip()
  fpsClock.tick(fps)
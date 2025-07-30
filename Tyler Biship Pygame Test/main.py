# --------------------------------------
# Title: boilerplate.py
# Purpose: Basic boilerplate code for pygame
# Author: Sarah Herzog
# Date: 12/05/2023
# --------------------------------------



# --------------------------------------
# Import Libraries
# --------------------------------------
import pygame
# --------------------------------------
from player import Player
myplayer = Player()
# --------------------------------------
# Initialisation and Setup
# --------------------------------------
# Initialize python so we can use it
pygame.init()

# Set up the game clock
mainClock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('red cube of world domination')

# Set up some variables to use later in our game
running = True
# END of Initialisation and Setup
# --------------------------------------


# --------------------------------------
# Game Loop
# --------------------------------------
# Run over and over until the user asks to quit
while running:
    
    # ----------------------------------
    # Input
    # ----------------------------------
    # Did the user click the window close button?
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            running = False
    # END of Input
    # ----------------------------------

    
    # ----------------------------------
    # Update
    # ----------------------------------
    # TODO: Update the game logic here!
    # END of Update
    # ----------------------------------
    myplayer.update(all_events)

    
    # ----------------------------------
    # Draw
    # ----------------------------------
    # Fill the background with a colour
    screen.fill((168, 38, 255))

    # Draw Everything
    # TODO: Draw all your sprites here!
    myplayer.draw(screen)

    # Flip the display
    pygame.display.flip()
    # END of Draw
    # ----------------------------------

# END of Game Loop
# --------------------------------------


# --------------------------------------
# Program Exit
# --------------------------------------
pygame.quit()
# --------------------------------------
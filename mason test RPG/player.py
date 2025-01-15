import pygame
from pygame import Rect, Vector2
import pygame_gui

pressed_key = {"left" : False, "right" : False}

class Player:

    def __init__(self):
        return

    # input checking
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pressed_key["left"] = True
                if event.key == pygame.K_d:
                    pressed_key["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    pressed_key["left"] = False
                if event.key == pygame.K_d:
                    pressed_key["right"] = False
                
"""

FOR COMBAT SECTION
engage with enemy

battle starts
player turn first (simplicity change later)
    on players turn
    menu opens up with major options (attack, defend, magic, items, flee, etc)
        with major option selected:
        attack:
            a data structure to store all attacks
            choose attack from list
            deal damage if hit, update state of enemy etc
            update state of player (hp drain or mana drain)
        magic:
            same deal
            elemental weaknesses???'
            crit chance??
            merge with atttack? how are these different?
            defensive spells, buffs, etc
        unique system mechanic choice ie persona, limit, etc..
        flee
            % chance to leave the battle
        item:
            similar data structure to attacks?
            choose item, apply affect
            limited resource
        defend??
            reduce damage maybe not affected by weakness?

enemy turn:
    each enemy pulls from a move list
    give certian enemies prefences/ai maybe some prefer buffing over attacking? etc
    no defend, no flee, no system mechanic



        

"""
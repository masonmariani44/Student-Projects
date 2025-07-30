import pygame

class Attacks_P1:

    def __init__(self):

        #attack assignment
        self.attacks = {

            "idle" : [pygame.image.load("animations/idle/1.png")],

            "jab" : [pygame.image.load("p1_attacks/neutral_air/1.png"), 
                     pygame.image.load("p1_attacks/neutral_air/2.png"), 
                     pygame.image.load("p1_attacks/neutral_air/3.png"), 
                     pygame.image.load("p1_attacks/neutral_air/4.png")]

        }

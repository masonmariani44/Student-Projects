import pygame
from pygame import Rect, Vector2
pressed_key = {"left" : False, "right" : False, "up" : False}

FRICTION_CONST = .75
WALK_CONST = 1
SPEED_LIMIT_X = 10
SPEED_LIMIT_Y = 10

class Player:


    def __init__(self):
        self.rect = Rect(300, 0, 30, 50)
        self.velocity = Vector2(0,0)
        self.on_ground = False

        #attack assignment
        self.attacks = {}
        #self.attacks["up_air"] = Attack()


    def update(self, all_events):

        #gravity update
        self.velocity += Vector2(0,1)

        # check if on ground!!!!!
        # FRICTION
        if self.velocity.x > -1 and self.velocity.x < 1:
            self.velocity.x = 0

        if self.velocity.x > 0:
            self.velocity -= Vector2(FRICTION_CONST, 0)
        if self.velocity.x < 0:
            self.velocity += Vector2(FRICTION_CONST, 0)

        """
        pick a button for each attack type
        """

        # check for player input
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pressed_key["left"] = True
                if event.key == pygame.K_d:
                    pressed_key["right"] = True
                if event.key == pygame.K_w:
                    pressed_key["up"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    pressed_key["left"] = False
                if event.key == pygame.K_d:
                    pressed_key["right"] = False
                if event.key == pygame.K_w:
                    pressed_key["up"] = False
        #if pygame.key.get_pressed() == "W":


        #if pygame.key.get_pressed() == "S":

        # TODO LAST TIME: we were adding jumping. doesnt jump rn
        if pressed_key["left"] is True:
            self.velocity += Vector2(-1 * WALK_CONST, 0)
        if pressed_key["right"] is True:
            self.velocity += Vector2(WALK_CONST, 0)
        if pressed_key["up"] is True:
            self.velocity += Vector2(0, -50)

        # speed cap section
        if self.velocity.x > SPEED_LIMIT_X:
            self.velocity.x = SPEED_LIMIT_X
        if self.velocity.x < -1 * SPEED_LIMIT_X:
            self.velocity.x = -1 * SPEED_LIMIT_X
        if self.velocity.y > SPEED_LIMIT_Y:
            self.velocity.y = SPEED_LIMIT_Y
        if self.velocity.y < -1 * SPEED_LIMIT_Y:
            self.velocity.y = -1 * SPEED_LIMIT_Y

        if self.on_ground is True:
            self.velocity.y = 0

        """
        attack check section

        w is pressed and normal attack (j) is pressed
            w + j in air -> up air

        """


        self.rect.center = Vector2(self.rect.center) + self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen,(255,0,0), self.rect)
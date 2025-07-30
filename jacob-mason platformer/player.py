import pygame
from pygame import Rect, Vector2

pressed_key = {"left" : False, "right" : False}


GRAVITY = 1
WALK_SPEED = 1
Y_SPEED_LIMIT = 30

class Player:

    def __init__(self):
        self.rect = Rect(300, 0, 30, 50)
        self.velocity = Vector2(0, 0)
        self.on_ground = False

    def update(self, events):

        # this is our gravity
        self.velocity += Vector2(0, GRAVITY)

        #friction (TODO)

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

        if pressed_key["left"]:
            self.velocity += Vector2(-WALK_SPEED, 0)
        if pressed_key["right"]:
            self.velocity += Vector2(WALK_SPEED, 0)

        # cap speed
        if self.velocity.y > Y_SPEED_LIMIT:
            self.velocity.y = Y_SPEED_LIMIT
        if self.velocity.y < -Y_SPEED_LIMIT:
            self.velocity.y = -Y_SPEED_LIMIT

        # ACTUALLY MOVES THE CHARACTER!!!!
        self.rect.center = Vector2(self.rect.center) + self.velocity


        """
        TODO for next time:
        vertical speed cap
        friction/air friction
        level creation
        collision
        """
        

        
        """
        
        apply gravity 

        apply friction

        check which key is being pressed
            move our guy by that much (in that direction)
            keep track of holding our button

        move and update pos

        """

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
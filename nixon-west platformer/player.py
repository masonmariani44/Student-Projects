import pygame
from pygame import Rect, Vector2

"""
TODO: 
do jumping
do wall collision
"""

class Player:

    def __init__(self):
        
        self.rect  = Rect(300, 0, 50, 50)

        self.velocity = Vector2(0, 0)

        self.on_ground = False

        self.SPEED_LIMIT_X = 10
        self.SPEED_LIMIT_Y = 10
        self.MOVE_ACCL = .7
        self.FRICTION_COEF = .5
        self.GRAVITY = .7

        self.key_pressed = { "left" : False, "right" : False }
        self.is_moving = False

    def handle_events(self, all_events, platforms):
        
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.key_pressed["right"] = True
                    self.is_moving = True
                if event.key == pygame.K_a:
                    self.key_pressed["left"] = True
                    self.is_moving = True
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    self.X = 10
                    self.key_pressed["right"] = False
                    self.is_moving = False
                if event.key == pygame.K_a:
                    self.key_pressed["left"] = False
                    self.is_moving = False
            
        
        if self.key_pressed["right"] == True:
            self.velocity += Vector2(self.MOVE_ACCL, 0)
        if self.key_pressed["left"] == True:
            self.velocity += Vector2(-self.MOVE_ACCL, 0)


        if self.velocity.x > self.SPEED_LIMIT_X:
            self.velocity.x = self.SPEED_LIMIT_X
        if self.velocity.x < -self.SPEED_LIMIT_X:
            self.velocity.x = -self.SPEED_LIMIT_X

        if self.velocity.y > self.SPEED_LIMIT_Y:
            self.velocity.y = self.SPEED_LIMIT_Y

        if not self.is_moving:
            if self.velocity.x > 0:
                self.velocity.x -= self.FRICTION_COEF
            else:
                self.velocity.x += self.FRICTION_COEF
        


        if not self.on_ground:
            self.velocity.y += self.GRAVITY



        if abs(self.velocity.x) < .5:
            self.velocity.x = 0




        for platform in platforms:
            if pygame.Rect.colliderect(self.rect, platform):

                # test above
                if self.rect.bottom > platform.top:
                    self.on_ground = True

                    self.velocity.y = 0
                    offset = (self.rect.bottom - platform.top) - 1
                    new_pos = Vector2(self.rect.center)
                    new_pos.y -= offset

                    self.rect.center = new_pos

                # TODO: wall collision

        if self.velocity.y != 0:
            self.on_ground = False


        self.rect.center = Vector2(self.rect.center) + self.velocity
    
    def draw(self, screen):
        player = pygame.draw.rect(screen, (255, 0, 0), self.rect)
        self.x = player.x
        self.y = player.y


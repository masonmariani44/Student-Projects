import pygame
from pygame import Rect, Vector2


class Player:

    def __init__(self, screen_x, screen_y):
        
        self.CHAR_X = 50
        self.CHAR_Y = 50

        self.rect = Rect(300, 300, self.CHAR_X, self.CHAR_Y)
        self.pressed_key = ""
        self.velocity = Vector2(0, 0)

        self.SCREEN_X = screen_x
        self.SCREEN_Y = screen_y

        self.x_pos = 0
        self.y_pos = 0


        self.MOVE_SPEED = .3

        self.tail = [Rect(0, 0, self.CHAR_X, self.CHAR_Y), Rect(0, 0, self.CHAR_X, self.CHAR_Y), Rect(0, 0, self.CHAR_X, self.CHAR_Y)]


    
    """

    TODO LIST

    we need to add boundaries to the screen 
    
    we also need to let steven know he is a really cool guy

    What do you call a dog missing 4 legs?
    It doesnt matter what you call it. its not coming to you

    Why did the vulture cross the road?
    Because the chicken didnt make it

    Steven is cool :P
    Steven is indeed cool <)
    ( -_•)▄︻デ══━一 IoI
    Steven totally didnt add these. You are so very kind for saying Steven is cool.

    """

    def update(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.pressed_key = "up"
                if event.key == pygame.K_a:
                    self.pressed_key = "left"
                if event.key == pygame.K_s:
                    self.pressed_key = "down"
                if event.key == pygame.K_d:
                    self.pressed_key = "right"

        if self.pressed_key == "up":
            self.velocity = Vector2(0, -self.MOVE_SPEED)
        if self.pressed_key == "left":
            self.velocity = Vector2(-self.MOVE_SPEED, 0)
        if self.pressed_key == "down":
            self.velocity = Vector2(0, self.MOVE_SPEED)
        if self.pressed_key == "right":
            self.velocity = Vector2(self.MOVE_SPEED, 0)

        self.x_pos += self.velocity.x
        self.y_pos += self.velocity.y


        self.rect.center = (self.x_pos, self.y_pos)
        

        

        if (self.x_pos - self.CHAR_X / 2) > self.SCREEN_X or (self.x_pos - self.CHAR_X / 2) < 0:
            print("out of bounds")
        if (self.y_pos - self.CHAR_Y / 2) > self.SCREEN_Y or (self.y_pos - self.CHAR_Y / 2) < 0:
            print("out of bounds")


    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

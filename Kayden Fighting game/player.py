import pygame
from pygame import Rect, Vector2
from attacks_p1 import Attacks_P1
pressed_key = {"left" : False, "right" : False, "up" : False, "down" : False, "normal" : False, "special" : False}
dirs = ["left", "right"]

FRICTION_CONST = .75
WALK_CONST = 1
SPEED_LIMIT_X = 10
SPEED_LIMIT_Y = 10

# TODO attack animations good resource. still need to mark player as attacking, then call function
# https://coderslegacy.com/python/pygame-rpg-attack-animations/


class Player:


    def __init__(self):
        self.rect = Rect(300, 0, 30, 50)
        self.velocity = Vector2(0,0)
        self.on_ground = False
        self.facing_dir = 1

        self.attacks = Attacks_P1()
        self.attacking = False
        self.attack_frame = 0
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
                if event.key == pygame.K_s:
                    pressed_key["down"] = True
                if event.key == pygame.K_k:
                    pressed_key["normal"] = True
                if event.key == pygame.K_l:
                    pressed_key["special"] = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    pressed_key["left"] = False
                if event.key == pygame.K_d:
                    pressed_key["right"] = False
                if event.key == pygame.K_w:
                    pressed_key["up"] = False
                if event.key == pygame.K_s:
                    pressed_key["down"] = False
                if event.key == pygame.K_k:
                    pressed_key["normal"] = False
                if event.key == pygame.K_l:
                    pressed_key["special"] = False
        #if pygame.key.get_pressed() == "W":


        #if pygame.key.get_pressed() == "S":

        # TODO we can jump, but there's no limit and we just fly
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

        # normals

        """ NOTE!!!!!! add a sperate jump button so we can do up tilts!!!!! up should be for direction of attack, jump should jump."""

        attack()





        self.rect.center = Vector2(self.rect.center) + self.velocity


    def attack(self):
        # TODO better organization... not happy about this
        if pressed_key["normal"] is True:
            # air normal
            if self.on_ground is False:
                if pressed_key[not self.facing_dir]:
                    # back air
                    pass
                elif pressed_key["up"]:
                    # up air
                    pass
                elif pressed_key["down"]:
                    # down air
                    pass
                else:
                    # forward air
                    pass
            # ground normal
            else:
                self.image = self.attacks.attacks[self.attack_frame]


    def draw(self, screen):
        pygame.draw.rect(screen,(255,0,0), self.rect)
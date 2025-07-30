import pygame
from pygame import Rect, Vector2
from attacks_p1 import Attacks_P1

pressed_key = {"left" : False, "right" : False, "up" : False, "down" : False, "normal" : False, "special" : False}
dirs = ["left", "right"]

FRICTION_CONST = .75
WALK_CONST = 1
SPEED_LIMIT_X = 10
SPEED_LIMIT_Y = 10

class Player:

    def __init__(self):
        #self.rect = Rect(300, 0, 30, 50)
        self.velocity = Vector2(0,0)
        self.on_ground = False
        self.facing_dir = 1

        self.animation_timer = 0
        self.attack_animation_frame = 0
        self.current_attack = None

        self.attacks = Attacks_P1()

        self.image = self.attacks.attacks["idle"][0]
        self.rect = self.image.get_rect()

        #attack assignment
       # self.attacks["up_air"] = Attack()
    
    def update(self, all_events, clock):
        #gravity update
        self.velocity += Vector2(0,1)

        if self.velocity.x > -1 and self.velocity.x < 1:
            self.velocity.x = 0

        if self.velocity.x > 1:
            self.velocity -= Vector2(FRICTION_CONST, 0)
        if self.velocity.x < -1:
            self.velocity += Vector2(FRICTION_CONST, 0)

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
                    print("presed k")
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
                        
        #if pygame.key.get_pressed() == "S":
            
        #if pygame.key.get_pressed() == "W":
            

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
        if self.velocity.y < -1 *  SPEED_LIMIT_Y:
            self.velocity.y = -1 * SPEED_LIMIT_Y

        if self.on_ground is True:
            self.velocity.y = 0







        # normals
        
        if pressed_key["normal"] is True and self.current_attack is None:

            # air normal
            if self.on_ground is False:
                if pressed_key[dirs[not self.facing_dir]]:
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
                self.current_attack = "jab"
                # set a state for our current animation, and if we should be animating something rn, we shouldnt even be here


                # he has the urgent note

        if self.current_attack is not None:
            self.animate_attack(clock, self.current_attack)
        else:
            # TODO we need seperation between animating attacks vs animating other things...
            self.animate_attack(clock, "idle")



        self.rect.center = Vector2(self.rect.center) + self.velocity

    
    def animate_attack(self, clock, given_attack):
        if self.attack_animation_frame >= len(self.attacks.attacks[given_attack]):
            self.attack_animation_frame = 0
            self.current_attack = None
            return False

        delta_time = clock.tick(30) / 1000.0
        self.animation_timer += delta_time

        self.image = self.attacks.attacks[given_attack][self.attack_animation_frame]
        self.attack_animation_frame += 1

        return True



    def draw(self, screen, surface):
        
        player_image = pygame.transform.scale(self.image, self.rect.size)
        player_image.convert()

        surface.blit(player_image, self.rect)
        screen.blit(surface, (0, 0))
        
        #pygame.draw.rect(screen,(255,0,0), self.rect)
        #pygame.Surface.blit(self.image, screen, self.rect)
        #screen.blit(screen, self.rect)
        




"""

update the player state so that we press a key once and an entire animation plays

make the stage load

clear last frame

cycle back to neutral animation

"""
import pygame

class Player:

    def __init__(self):
        self.power = 100

        self.left_door_closed = False
        self.right_door_closed = False
        self.left_light_on = False
        self.right_light_on = False
        self.camera_on = False

        self.camera_location = 0
    
    def update(self, all_events, night):

        """ Input Handling """
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                # if w is pressed, switch to cams
                if event.key == pygame.K_w:
                    self.camera_on = not self.camera_on
                # left light
                if event.key == pygame.K_q:
                    self.left_light_on = not self.left_light_on
                # right light
                if event.key == pygame.K_e:
                    self.right_light_on = not self.right_light_on
                # left door
                if event.key == pygame.K_a:
                    self.left_door_closed = not self.left_door_closed
                # right door
                if event.key == pygame.K_d:
                    self.right_door_closed = not self.right_door_closed

                    


        """ Update State """

        if self.left_door_closed:
            self.power -= night.door_power_drain
        if self.right_door_closed:
            self.power -= night.door_power_drain
        if self.left_light_on:
            self.power -= night.light_power_drain
        if self.right_light_on:
            self.power -= night.light_power_drain
        if self.camera_on:
            self.power -= night.camera_power_drain

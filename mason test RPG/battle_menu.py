import pygame_gui
import pygame

class Battle_Menu:

    def __init__(self, given_manager, width, height):
        self.manager = given_manager

        self.attack_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width*.05, height*.9), (width*.1875, height*.05)),
                                             text='Attack',
                                             manager=given_manager)
        self.defend_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((width*.05*2) + (width*.1875), height*.9), (width*.1875, height*.05)),
                                             text='Defend',
                                             manager=given_manager)
        self.magic_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((width*.05*3) + (width*.1875*2), height*.9), (width*.1875, height*.05)),
                                             text='Magic',
                                             manager=given_manager)
        self.item_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((width*.05*4) + (width*.1875*3), height*.9), (width*.1875, height*.05)),
                                             text='Item',
                                             manager=given_manager)
    
    def handle_events(self, all_events):
        for event in all_events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.attack_button:
                    print("Attack!!!")

            self.manager.process_events(event)
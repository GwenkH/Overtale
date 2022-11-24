import pygame, sys
from typing import List
from character import Character, Ability
from pygame.locals import MOUSEBUTTONDOWN

#Images
background_image = pygame.transform.scale(pygame.image.load("background.gif"),
                                          (600, 300))  #get bg image
panel_image = pygame.transform.scale(pygame.image.load("panel.png"),
                                     (600, 150))
menu_image = pygame.transform.scale(pygame.image.load("menu.png"),
                                    (600, 450))

buttons = []

class BattleScreen:

    def __init__(self, characters: List[Character],
                 enemies: List[Character]) -> None:
        self.width = 600
        self.height = 450
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Overtale')
        self.turn = 0
                
    def update(self) -> None:
        pass

    def draw(self, characters: List[Character],
             enemies: List[Character]) -> None: #Glenn-instance method takes argument

        #Background
        self.screen.blit(background_image, (0, 0))
        self.screen.blit(panel_image, (0, 300))

        GREEN = (0, 255, 0)
        #locations
        ally_x = [160, 0]
        enemy_x = [350, 450]
        character_y = 135
        health_bar_x = [160, 80]
        health_bar_x2 = [350, 450]
        health_bar_y = 100
                 
        ally_position = 0
        enemy_position = 0

        for character in characters:
            character.rect.center = (ally_x[ally_position], character_y)
            self.screen.blit(character.image, (ally_x[ally_position], character_y))
            
            #Health Bars
            pygame.draw.rect(self.screen, GREEN,
                             (health_bar_x[ally_position], health_bar_y,
                              character.health - (character.health/character.max_health), 20))
            ally_position += 1

        for enemy in enemies:
            enemy.rect.center = (enemy_x[enemy_position], character_y)
            self.screen.blit(enemy.image, (enemy_x[enemy_position], character_y))
            pygame.draw.rect(self.screen, GREEN, (health_bar_x2[enemy_position], health_bar_y, character.health, 20))
            enemy_position += 1
    
    # def ability_boxes(self) -> None:
        WHITE = (255, 255, 255)
        for x in range(100, 351, 250):
            for y in range(330, 381, 50):
                buttons.append(pygame.Rect(x, y, 180, 40))

        for i in range(len(buttons)):
            pygame.draw.rect(self.screen, WHITE, buttons[i])

        pygame.display.update()

            
            
    def attack_phase(self) -> None:
        if self.turn % 2 == 0:
          pass
            

    def click_event(self) -> None:
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
    
    def button_clicked(self, enemies: List[Character], enemy_num) -> None:
        self.click_event()
        mx, my = pygame.mouse.get_pos()
        pass    

      
    # def button_clicked(self, enemies: List[Character], enemy_num) -> None:
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #     if self.collidepoint((mouse_x, mouse_y)):
    #         self.ability(enemies[enemy_num])
            
    # def event_loop(self) -> None:
    #     events = pygame.event.get()
    #     for event in events:
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             clicked = True
    #             num = 0
    #             for button in buttons:
    #                 if button.collidepoint(event.pos) and clicked is True:
    #                     Character.abilities[num]
    #                     num += 1
                        
                
    #         else:
    #             clicked = False

    
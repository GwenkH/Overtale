from typing import List
import pygame, random
from game.overtale import Overtale
# from game.pause_view import PauseView
from game.base_view import BaseView
from game.character import Character, Ability
from game.inventory import Inventory


# color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
    

class BattleScreen(BaseView):
    # --
    buttons = []


    def __init__(self, characters: List[Character], enemies: List[Character]) -> None:
        self._knight = Character("knight", 100)
        self._enemy = Character("enemy", 100)
        self._party = [self._knight]
        self._enemies = [self._enemy]

        self._turn = 0
        self._characters = characters
        self._enemies = enemies
        self._target = self._enemies[0]
        self._selected_target = False
        self._clicked = False
        self._clicked_enemy_1 = False
        self._clicked_attack = False

        mx, my = pygame.mouse.get_pos()
        self._position = mx, my


        #Images
        self._background_image = pygame.transform.scale(pygame.image.load("background.gif"),
                                                (600, 300))  #get bg image
        self._panel_image = pygame.transform.scale(pygame.image.load("panel.png"),
                                            (600, 150))
        self._menu_image = pygame.transform.scale(pygame.image.load("menu.png"), (600, 450))


        # buttons
        self._button_1 = pygame.Rect(0, 0, 30, 30)
        self._button_2 = pygame.Rect(30, 0, 30, 30)
        self._button_3 = pygame.Rect(60, 0, 30, 30)
        self._enemy_1_area = pygame.Rect(388, 155, 30, 100)

        #locations
        self._ally_x = [160, 0]
        self._enemy_x = [350, 450]
        self._character_y = 135
        self._ally_position = 0
        self._enemy_position = 0


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_p:
                    """pause"""
                    pass
    
    def update(self) -> None:
        if self._enemy_1_area.collidepoint((self._position)):
            if self._clicked == True:
                self._clicked_enemy_1 = True
        
        if self._clicked_enemy_1 == True:
            self._target = self._enemies[0]
            self._selected_target = True
            print("selected")

        if self._clicked == True:
            self._clicked_attack = True

        if self._button_1.collidepoint((self._position)):                                 
            if self.clicked_attack == True:
                Ability.heavy_hit(self.target)
                print("")

        pygame.display.update()
        if self._button_2.collidepoint((self._position)):
            if self.clicked_attack:
                Ability.critical_stab(self, self._target)

        pygame.display.update()
        if self._button_3.collidepoint((self._position)):
            if self.clicked_attack:
                Ability.shield(self)

        pygame.display.update()
        for member in self._enemies:
            member.update()
        for member in self._party:
            member.update()

    def draw(self, surface: pygame.Surface) -> None: 
        """Draws background and characters."""
        #Background
        surface.blit(self._background_image, (0, 0))
        surface.blit(self._panel_image, (0, 300))

        # painting
        pygame.draw.rect(surface, BLUE, (0, 0, 30, 30), 5)
        pygame.draw.rect(surface, RED, (30, 0, 30, 30), 5)
        pygame.draw.rect(surface, GREEN, (60, 0, 30, 30), 5)

        for character in self._party:
            character.get_rect().center = (self._ally_x[0], self._character_y)
            surface.blit(character.get_image(),
                                (self._ally_x[0], self._character_y))

            self._ally_position += 1

        for enemy in self._enemies:
            enemy.get_rect().center = (self._enemy_x[0], self._character_y)
            surface.blit(enemy.get_image(),
                                (self._enemy_x[0], self._character_y))

            self._enemy_position += 1


        pygame.display.update()


    def attack_phase(self, target: Character, target_enemy: Character) -> None:
        """makes turns and dictates who attacks each turn
        
        Args:
            target(Character): user being the target of the ability
            enemy_target(Character): enemy being target of ability

        Return:
            None
        """
        if self._turn % 2 == 0:
            target.select_target()
            ability_use = target.attack_hit()
            target.do_attack(target_enemy, ability_use)
            self._turn += 1
        else:
            ability_use = random.choice(self.enemy.get_abilities())
            target_enemy.do_attack(target, ability_use)
            self._turn += 1

    def use_item(self, target: Character) -> None:
        self.position = pygame.mouse.get_pos()

        item_button = pygame.Rect(500, 350, 30, 30)

        if item_button.collidepoint((self._position)):
            Inventory.items[0](target)
            Inventory.items.remove(Inventory.items[0])


class HealthBar:

    def __init__(self, x: int, y: int, party: List[Character],
                 enemies: List[Character], char_in_list: int) -> None:
        '''
        Initializes HealthBar objects

        Args:
            x (int): x position of the healthbar
            y (int): y position of the healthbar
            hp (int): max hp and initial hp
            party (list): list of characters
            enemies (list): list of enemy characters
        
        Returns:
            None
        '''
        self._max_hp = party[char_in_list].get_health()
        self._hp = party[char_in_list].get_health()
        self._x = x
        self._y = y
        self._party = party
        self.screen = BattleScreen(party, enemies).screen

    def event_loop(self) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        '''
        Draws Healthbars

        Args:
            None

        Returns:
            None
        '''
        pygame.draw.rect(self.screen, RED,
                         (self._x, self._y, self._max_hp, 20))  #Red bar

        pygame.draw.rect(
            self.screen, GREEN,
            (self._x, self._y,
             (self._hp / self.max_hp) * self._max_hp, 20))  #Green bar

    # def select_target(self) -> None:  # Esther A2.3
    #     """select the target"""
        # # click event
        # clicked_enemy = False
        # mx, my = pygame.mouse.get_pos()
        # self.click_battle()

        # # get enemy area
        # enemy_1_area = pygame.Rect(388, 155, 30, 100)

        # if enemy_1_area.collidepoint((mx, my)):
        #     if self.clicked == True:
        #         clicked_enemy = True
        #     if clicked_enemy_1 == True:
        #         self.target = self.clickedenemies[0]
        #         self.selected_target = True
        #         print("selected")
        # pygame.display.update()

    # def hit_attack(self):  # Esther A2.3
    #     """do damage to the target"""
    #     pygame.display.update()
    #     # clicked_attack = False
    #     # ax, ay = pygame.mouse.get_pos()
    #     # self.click_battle()
    #     if self.clicked == True:
    #         clicked_attack = True
        # # creat buttons
        # button_1 = pygame.Rect(0, 0, 30, 30)
        # button_2 = pygame.Rect(30, 0, 30, 30)
        # button_3 = pygame.Rect(60, 0, 30, 30)

        # button click conditions
        # if button_1.collidepoint((ax, ay)):
        #     if clicked_attack == True:
        #         Ability.heavy_hit(self.target)
        #         print("do damage")

        # pygame.display.update()
        # if button_2.collidepoint((ax, ay)):
        #     if clicked_attack:
        #         Ability.critical_stab(self, self.target)

        # pygame.display.update()
        # if button_3.collidepoint((ax, ay)):
        #     if clicked_attack:
        #         Ability.shield(self)
        # pygame.display.update()

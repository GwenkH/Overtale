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
        self._health_bar_y = 100
        
        #hp bars
        self._character_hp = HealthBar(self._ally_x[self._ally_position], self._health_bar_y, self._characters[0])
        self._enemy_hp = HealthBar(self._enemy_x[self._enemy_position], self._health_bar_y, self._enemies[0])


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_p:
                    """pause"""
                    pass
                if event.key == pygame.locals.K_e:
                    self.open_inventory = True
                    Overtale.set_current_view(Inventory(self))

            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self._enemy_1_area.collidepoint(event.pos):
                    print("selected target")
                    self._selected_target = True
                    player_1 = Player()
                    target = self._enemies[0]
                    player_1.set_target(target) # UNDEFINED METHOD

                if self._button_1.collidepoint(event.pos):
                    print("heavy_hit")
                    self._characters[0].do_attack(self._enemies[0], 0)

                if self._button_2.collidepoint(event.pos):
                    print("critical_stab")
                    self._characters[0].do_attack(self._enemies[0], 1)
                    
                if self._button_3.collidepoint(event.pos):
                    print("shield")
                    self._characters[0].do_shield()
                    
                self._turn += 1

                # if (self._turn % 2) == 1:
                #     self.attack_phase(self._characters[0], self._enemies[0])
                #     print("asdfj")
                        
    
                for character in self._characters:
                    if character.get_health() <= 0:
                        """run endscreen"""
                        pass

                for enemy in self._enemies:
                    if enemy.get_health() <= 0:
                        pass
    
    def update(self) -> None:
        pass
        

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
            
            character.animate()
            self._character_hp.draw(surface)

            self._ally_position += 1

        for enemy in self._enemies:
            enemy.get_rect().center = (self._enemy_x[0], self._character_y)
            surface.blit(enemy.get_image(),
                                (self._enemy_x[0], self._character_y))
            
            enemy.animate()
            self._enemy_hp.draw(surface)

            self._enemy_position += 
            
    def get_turn(self) -> int: 
        """Returns current turn number
        
        Returns:
            int: the current turn number
        """
        return self._turn

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
        self._hp = self._character.get_health()
        
        pygame.draw.rect(self.screen, RED,
                         (self._x, self._y, self._max_hp, 20))  #Red bar

        pygame.draw.rect(
            self.screen, GREEN,
            (self._x, self._y,
             (self._hp / self.max_hp) * self._max_hp, 20))  #Green bar
        
        

class AbilityButtons(BaseView):
    
    def __init__ (self, x: int, y: int, character_ability: Character):
        
        self._x = x
        self._y = y
        self._character = character_ability
        self._character_ability = character_ability.get_abilities()
        pass


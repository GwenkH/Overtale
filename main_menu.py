import pygame, sys
from game.base_view import BaseView
from game.battle_screen import BattleScreen
from game.overtale import Overtale
from game.character import Character
from game.player import Player


class MainMenu(BaseView):
    def __init__(self) -> None:
        self.mx, self.my = pygame.mouse.get_pos()
        menu_font = pygame.font.Font('undertale.ttf', 40)
        self.menu_text = menu_font.render("OVERTALE", True, (255, 255, 255))
        self.menu_image = pygame.transform.scale(pygame.image.load("menu.png"), (600, 450))
        self.select_knight = pygame.transform.scale(pygame.image.load('knight9.png'), (200, 240)) 
        self.select_enemy = pygame.transform.scale(pygame.image.load('enemy/enemy~.png'), (177, 233))

        # these shouldnt be there
        self.knight = Character("knight", 100)
        self.enemy = Character("enemy", 100)
        self.party = [self.knight] 
        self.enemies = [self.enemy]

        # self._click_knight = False
        # self._click_enemy = False

    def event_loop(self, events) -> None: 
        for event in events:
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                select_knight_area = self.select_knight.get_rect(topleft=(88, 155))
                select_enemy_area = self.select_enemy.get_rect(topleft=(333, 177))

                # generate the knight needa change
                if select_knight_area.collidepoint(event.pos):
                    player_1 = self.knight
                    player_1._party.append(player_1)
                    player_2 = self.enemy
                    player_2._enemies.append(player_2)
                    Overtale.set_current_view(BattleScreen(self.party, self.enemies))
                    # and who ever the player clicked will attack first
                  
                if select_enemy_area.collidepoint(event.pos):
                    enemy_1 = Player(self.enemy)
                    player_1.enemies.append(enemy_1)
                    Overtale.set_current_view(BattleScreen(self.party, self.enemies))
              

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    def update(self) -> None: 
        """charater the player is controling"""
        pass

    def draw(self, surface: pygame.Surface) -> None:
        """drawing the title screen"""
        surface.blit(self.menu_image, (0, 0))
        surface.blit(self.menu_text, (60, 140))
        surface.blit(self.select_knight, (88, 155))
        surface.blit(self.select_enemy, (333, 177))

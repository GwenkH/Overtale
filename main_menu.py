import pygame, sys
from game.base_view import BaseView
from game.battle_screen import BattleScreen
from game.overtale import Overtale
from game.character import Character


class MainMenu(BaseView):
    def __init__(self) -> None:
        self.mx, self.my = pygame.mouse.get_pos()
        menu_font = pygame.font.Font('undertale.ttf', 40)
        self.menu_text = menu_font.render("OVERTALE", True, (255, 255, 255))
        self.menu_image = pygame.transform.scale(pygame.image.load("menu.png"), (600, 450))
        self.select_knight = pygame.transform.scale(pygame.image.load('knight9.png'), (200, 240)) 
        self.select_enemy = pygame.transform.scale(pygame.image.load('enemy/enemy~.png'), (177, 233))
        # self.select_enemy_area = self.select_enemy.get_rect(topleft=(333, 177))
        self.knight = Character("knight", 100)
        self.enemy = Character("enemy", 100)
        self.party = [self.knight]
        self.enemies = [self.enemy]

        self.clicked = False
        self.click_knight = False
        self.click_enemy = False

    def event_loop(self, events) -> None: 
        for event in events:
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                ax, ay = pygame.mouse.get_pos()
                select_knight_area = self.select_knight.get_rect(topleft=(88, 155))
                if select_knight_area.collidepoint((ax, ay)):
                    Overtale.set_current_view(BattleScreen(self.party, self.enemies))

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.clicked = True
            # # quit
            # if event.type == pygame.QUIT:
            #     pygame.quit()
            #     sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         pygame.quit()
            #         sys.exit()


    def update(self) -> None: 
        """charater the player is controling"""
        # select_knight_area = self.select_knight.get_rect(topleft=(88, 155))
        ax, ay = pygame.mouse.get_pos()
        select_knight_area = self.select_knight.get_rect(topleft=(88, 155))
        if select_knight_area.collidepoint((ax, ay)):
            # if self.clicked == True:
            #     self.click_knight == True
            # if self.click_knight == True:
                """the character is knight"""
                knight_1 = Character("knight", 100)
                self.party.append(knight_1)

            # if self.click_enemy == True:
            #     """the character is enemy"""
            #     pass

    def draw(self, surface: pygame.Surface) -> None: 
        surface.blit(self.menu_image, (0, 0))
        surface.blit(self.menu_text, (60, 140))
        surface.blit(self.select_knight, (88, 155))
        surface.blit(self.select_enemy, (333, 177))

        # if self.clicked == True:
        #     """display battle screen"""
        #     battle = BattleScreen(self.party, self.enemies)
        #     # enemy_hp.draw()
        #     # knight_hp.draw()
        #     battle.draw()
            


    
    # def click_menu(self) -> None:
    #     """check if the button in main_menu has been clicked"""
    #     pass

    # def select_character(self) -> None:
    #     """click the character to select, then start the game"""
      
    #     if self.select_knight_area.collidepoint((self.mx, self.my)):
    #         self.click_menu()
    #         while self.clicked == True:
    #             """display battle screen"""
    #             battle = BattleScreen(self.party, self.enemies)
    #             # enemy_hp.draw()
    #             # knight_hp.draw()
    #             battle.draw()
                
    #             for member in self.party:
    #                 member.update()
    #             for member in self.enemies:
    #                 member.update()
                    
                
    #             pygame.display.update()
    #             self.clicked == False

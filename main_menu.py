import pygame, sys
from battle_screen import BattleScreen
from character import Character
# load
menu_image = pygame.transform.scale(pygame.image.load("menu.png"), (600, 450))
# select_bar_1 = pygame.transform.scale(pygame.image.load('testing_area.png'), (300, 50))
select_knight = pygame.transform.scale(pygame.image.load('knight9.png'), (200, 240)) 
select_enemy = pygame.transform.scale(pygame.image.load('enemy/enemy~.png'), (177, 233))

# --
knight = Character("knight", 100)
knight.define_abilities()
# knight_2 = Character("knight", 120)
# knight_2.define_abilities()
enemy = Character("enemy", 80)
enemy.define_abilities()

party = [knight]
enemies = [enemy]

# class
class MainMenu: 
  def __init__(self) -> None:
    self.screen = pygame.display.set_mode((600, 450))
    pygame.display.set_caption('Overtale')
    self.clicked = False
    # self.select_1 = select_bar_1.get_rect(topleft=(0, 300))

  def display_menu(self) -> None:
    self.screen.blit(menu_image, (0,0))
    font = pygame.font.Font('undertale.ttf', 40)
    text = font.render("OVERTALE", True, (255, 255, 255))
    self.screen.blit(text, (60, 140))
    self.screen.blit(select_knight, (88, 155))
    self.screen.blit(select_enemy, (333, 177))
    
    # self.screen.blit(select_bar_1,(0, 120))
    

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

  def select_character(self):
    mx, my = pygame.mouse.get_pos()
    select_knight_area = select_knight.get_rect(topleft=(88, 155))
    # select_enemy_area = select_enemy.get_rect(topleft=(333, 177))

    if select_knight_area.collidepoint((mx, my)):
      self.click_event()
      while self.clicked == True:
        """display battle screen"""
        battle = BattleScreen(party, enemies)
        battle.draw(party, enemies)
        for member in party:
            member.update()
        for member in enemies:
            member.update()
            pygame.display.update()
            self.clicked == False
    
    # if select_enemy_area.collidepoint((mx, my)):
    #   while self.clicked == True:
    #     """display battle screen"""
    #     battle = BattleScreen(party, enemies)
    #     battle.draw(party, enemies)
    #     pygame.display.update()
    #     self.clicked == False
    
    pygame.display.update()
    

    
  # def _main_menu(self, click: bool):
  #   click = False
  #   while True:
  #     # display menu background and character images
  #     self.screen.blit(self.menu_image, (0,0))
      
  #     # get mouse positions 600 450
  #     mx, my = pygame.mouse.get_pos()

  #     # create select area
  #     select_1 = select_bar_1.get_rect(topleft=(0, 300))

  #     # select area click conditions
  #     if select_1.collidepoint((mx, my)):
  #       if click: # if click go to battle page
  #         pass
  #         # event_loop(BattleScreen())

  #     # keyboard and mouse controls
  #     click = False
  #     for event in pygame.event.get():
  #       if event.type == pygame.QUIT:
  #         pygame.quit()
  #         sys.exit()
  #       if event.type == pygame.KEYDOWN:
  #         if event.key == pygame.K_ESCAPE:
  #             pygame.quit()
  #             sys.exit()
  #       if event.type == pygame.MOUSEBUTTONDOWN:
  #         if event.button == 1:
  #            click = True

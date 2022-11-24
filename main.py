import pygame, sys
from pygame.locals import QUIT
from character import Character
# from battle_screen import BattleScreen
# from inventory import Inventory, Item
from main_menu import MainMenu
# from main_menu import MainMenu

#Initializing Pygame
pygame.init()

#Screen
width = 600
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Overtale')

#Images
background_image = pygame.transform.scale(pygame.image.load("background.gif"),
                                          (600, 300))  #get bg image
panel_image = pygame.transform.scale(pygame.image.load("panel.png"),
                                     (600, 150))
menu_image = pygame.transform.scale(pygame.image.load("menu.png"), (600, 450))
# select_bar_1 = pygame.transform.scale(pygame.image.load('testing_area.png'), (300, 50))
select_knight = pygame.transform.scale(pygame.image.load('knight9.png'), (200, 240)) 
select_enemy = pygame.transform.scale(pygame.image.load('enemy/enemy~.png'), (177, 233))



#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
AQUA = (127, 255, 212)
BLUE = (0, 0, 255)




# knight = Character("knight", 100)
# enemy = Character("enemy", 100)


# party = [knight]
# enemies = [enemy]


# ----------Main Program Loop----------
clock = pygame.time.Clock()
run = True

while run:
    
    clock.tick(60)
    
    menu = MainMenu()
    menu.display_menu()
    menu.select_character() #Chooses character, runs battlescreen
  
    attack = False
    target = None

    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()
    

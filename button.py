import pygame
from character import Character


class Button:

    def __init__(self, x: int, y: int, ability_num: int) -> None:
        self.ability = Character.get_abilities()[ability_num]
        self.x = x
        self.y = y
        width = pygame.image.load()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width, height))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
        

    def button_clicked(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.collidepoint((mouse_x, mouse_y)):
            self.ability(enemy)

    

    def draw(self, screen):
        action = None
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse clicked on button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = 

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

import pygame, sys
from typing import List
from game.character import Character
from game.base_view import BaseView
from game.overtale import Overtale

# color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
THIS = (127, 255, 212)

class Item:
    def __init__(self, name: str):
      self.name = name
      self.amount = 0

    def __str__(self) -> str:
      return self.name

    def health_potion(self, target: Character) -> None: 
        target.health += 50

    def rage_potion(self, target: Character) -> None:
        for ability in range(len(target.abilities)):
            target.abilities[ability].damage += 10


class Inventory(BaseView):
  def __init__(self, parent: BaseView):
    self._capacity = 6
    self._items = [Item("health potion"), Item("rage potion")] # list
    self.position = 1
    self.current_num = self.position - 1
    self.current_item = self._items[self.current_num] # Item

    # --
    self.parent = parent
    self.font = pygame.font.Font('undertale.ttf', 33)
    self.text_font = pygame.font.Font('undertale.ttf', 20)
    self.text = self.font.render("Inventory", True, WHITE)

    self._name = "Inventory"
    self._locked = True
    # self.player_self = Character()
          
  def event_loop(self, events: List[pygame.event.Event]):
      for event in events:
          if event.type == pygame.locals.KEYDOWN:
              if event.key == pygame.locals.K_RETURN:

                if self.current_item.name == "health potion":
                  print("2:33")
                  # self.current_item.health_potion()
                  pass

                if self.current_item.name == "rage potion":
                  print("3:22")
                  pass

                print("2:38")
                self.current_item.amount -= 1


              # go back
              if event.key == pygame.locals.K_e:
                  Overtale.set_current_view(self.parent)
              
              # quit
              if event.key == pygame.locals.K_q:
                  from game.main_menu import MainMenu
                  # menu = MainMenu()
                  # menu.set_previous_score(self.parent.score)
                  Overtale.set_current_view(MainMenu)
              
              # select
              if event.key == pygame.locals.K_1:
                # use the first item in list
                self.num = 1
                self.position = 1
                self.current_item = self._items[self.num]
                
                pass

              if event.key == pygame.locals.K_2:
                self.position = 2


  def update(self) -> None:
     pass


  def draw(self, surface: pygame.Surface) -> None:
    # draw parent screen
    self.parent.draw(surface)

    # option bar
    pygame.draw.rect(surface, BLACK, (200, 60, 252, 360))
    pygame.draw.rect(surface, WHITE, (200, 60, 251, 360), 5)

    # 1
    pygame.draw.rect(surface, BLUE, (200, 60, 251, 60), 5)
    abc = str(self._items[0])
    option_1 = self.text_font.render(abc, True, WHITE)
    surface.blit(option_1, (233, 75))

    # 2
    efg = str(self._items[1])
    option_2 = self.text_font.render(efg, True, WHITE)
    surface.blit(option_2, (233, 135))


    # use-info-drop
    pygame.draw.rect(surface, BLUE, (200, 360, 251, 60), 5)
    pygame.draw.rect(surface, BLUE, (200, 360, 84, 60), 5)
    pygame.draw.rect(surface, THIS, ((284, 360, 84, 60)), 5)
    pygame.draw.rect(surface, BLUE, (368, 360, 84, 60), 5)


    # draw cursor
    cx = 10 + 200
    cy = 10 + (60 * (self.position))
    cursor = self.font.render(">", True, RED)
    surface.blit(cursor, (cx, cy))


  def add_item(self, type: Item) -> None:
    self._items.append(Item)
  def remove_item(self, item: Item)-> None:
    self._items.remove(item)
    pass
  def create_inventory():
    """match the inventory with character"""
    pass

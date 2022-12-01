# from typing import List
from game.character import Character

class Item: # have the chances to collect and use the items during the game? maybe
  # or inventory has an owner asasdasdhqdiuwashdausjddnhqwduashkuqwdy
    def __init__(self):
      pass

    def health_potion(self, target: Character) -> None:
      # can change it to if use call a function in ability class
      # and ability will have arg target? 
        target.health += 50

    def rage_potion(self, target: Character) -> None:
        for ability in range(len(target.abilities)):
            target.abilities[ability].damage += 10


    
        
class Inventory: #
    def __init__(self,owner,capacity: int, locked: bool) -> None:
        """
        Initializes Inventory object

        Args:
            owner(Character): a character object who owns the inventory
            capacity(int):capacity of inventory
            items(List[items]):List of items in item class
        Returns:
            None
        """
        self._owner = Character() # no
        self._capacity = capacity
        self._items = []
        self._name = "Inventory"
        self._locked = False
        # self._lock_combo = None

    def add_item(self, type: Item) -> None:
        self._items.append(Item)
    def remove_item(self, item: Item)-> None:
      self._items.remove(item)
      pass
    # def set_combo(self)-> None:
    #   pass
    # def lock():
    #   pass
    # def unlock():
    #   pass
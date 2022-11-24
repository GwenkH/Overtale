from typing import List
from character import Character

class Item:

    def health_potion(self, target: Character) -> None:
        target.health += 50

    def rage_potion(self, target: Character) -> None:
        for ability in range(len(target.abilities)):
            target.abilities[ability].damage += 10
        
class Inventory:

    def __init__(self, capacity: int, items: List[Item]) -> None:
        self.capacity = capacity
        self.items = items
        self.name = "Inventory"

    def add_item(self, type: str) -> None:
        self.items.append(Item.type)
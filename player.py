import pygame, sys
from game.character import Character
from game.inventory import Inventory


class Player:
    def __init__(self):
        self._player_number = 0

        self._character = None
        self._item = None
        self._inventory = None

        self._have_target = False #??
        self._target = None

    # esther c1.2
    def set_character(self, character: Character) -> None:
        self._character = character
        return {self._character}

    def set_inventory(self, inventory: Inventory) -> None:
        self._inventory = inventory
        

    def set_target(self, target: Character) -> None:
        self._target = target
        self._have_target = True
        

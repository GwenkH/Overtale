import pygame
import random
from pygame import *

#Classes
class Character:

    def __init__(self, type: str, health: int) -> None:
        """Creates a character.
        
        Args: 
            type (str): The type of character that is being created.
            health (int): The amount of health the character will have.
        """
        self._type = type
        self._health = health
        self._max_health = health
        self._shield = 10
        self._alive = True
        self._abilities = []
        self._animations = []
        self._frame = 0
        self._action = 0  #0:idle, 1: attack, 2: block, 3: die
        self.last_update = pygame.time.get_ticks()
        # self.inventory? aggregation

        #generate idle images
        action_list = []
        for image in range(4):
            img = pygame.transform.scale(
                pygame.image.load(f"{self._type}/idle_{image}.png"), (100, 125))
            action_list.append(img)
        self._animations.append(action_list)
        self._image = self._animations[self._action][self._frame]

        self._rect = self._image.get_rect()
        self.define_abilities()
        print(self.get_type())

    def get_health() -> int:
        return(self.max_health)
    
    def take_damage(self, amount: int) -> None:
        """Makes the character lose health by damage

        Args:
            amount (int): the amount of damage the character takes
        """
        if amount > self._health:
            self._health = 0
            self._alive = False

        if amount > self._health:
            self._health -= amount

    def set_shield(self, amount: int) -> None:
        """Changes the character's shield amount
        
        Args:
            amount (int): the amount that the character's shield gains or loses
        """
        self._shield += amount

    def get_type(self) -> str:
        """Returns the character type as a string.

        Returns:
            str: character type 
        """
        return f"Generated {self._type}"

    def get_image(self) -> pygame.image:
        """Returns current frame of character animation
        
        Returns: 
            pygame.image: the current image of the character
        """
        return self._image

    def get_rect(self) -> pygame.Rect:
        """Returns the character's rectangle

        Returns:
            pygame.Rect: the rectangle assigned to the character's image
        """
        return self._rect

    def update(self) -> None:  
        """Creates character image animation loop."""
        animation_cd = 300
        #update image
        self._image = self._animations[self._action][self._frame]
        #time check
        if pygame.time.get_ticks() - self.last_update > animation_cd:
            self.last_update = pygame.time.get_ticks()
            self._frame += 1
        #animation loop reset
        if self._frame >= len(self._animations[self._action]):
            self._frame = 0


    def define_abilities(self) -> None: 
        """Gives character abilities specified to its type."""
        if self._type == "knight":
            self._abilities = [Ability.heavy_hit, Ability.critical_stab]
        if self._type == "wizard":
            self._abilities = [
                Ability.special_ability, Ability.special_ability_2
            ]
        if self._type == "enemy":
            self._abilities = [
                Ability.enemy_basic_attack, Ability.enemy_special_attack
            ]
            
    def do_attack(self, target: 'Character', attack: 'Ability') -> None:
        """Does ability on chosen character.
        
        Args:
            target (Character): the target of the chosen ability
            attack (Ability): the specified ability to use
        """
        self._action = 1
        attack(target)
        
    def open_inventory(self) -> None:  #open menu for items
        pass

    def get_abilities(self) -> list:
        return (self._abilities)



class Ability:

    def __init__(self):
        pass

    @staticmethod
    def heavy_hit(target: Character) -> None:  
        """Ability for knight character which deals damage.

        Args:
            target (Character): The character that will receive damage.
        """
        name = "Heavy Hit"
        damage = 40
        target.take_damage(damage)

    @staticmethod
    def critical_stab(target: Character) -> None:
        """Ability for knight character which deals random damage.

        Args:
            target (Character): The character that will receive damage.
        """
        name = "Critical Stab"
        damage = random.randint(20, 70)
        target.take_damage(damage)


    @staticmethod
    def shield(
            target: Character) -> None:  #reduce incoming damage from one enemy
        """Ability for character that reduces damage taken.
        
        Args:
            target (Character): The character that will reduce damage taken.
        """
        name = "Shield"
        target.set_shield(20)

    def special_ability(self, target: Character) -> None:
        pass

    def special_ability_2(self, target: Character) -> None:
        pass

    @staticmethod
    def enemy_basic_attack(target: Character) -> None:
        """Ability for enemy character which deals damage.
        
         Args:
            target: The character that will receive damage.
        """
        name = "Slash"
        damage = random.randint(40)
        target.take_damage(damage)

    @staticmethod
    def enemy_special_attack(target: Character) -> None:
        """Ability for enemy character which deals damage that avoids shields.
        
         Args:
            target: The character that will receive random damage.
        """
        name = "Piercing Strike"
        damage = random.randint(30, 50)
        target.take_damage(damage)

    @staticmethod
    def enemy_special_ability(target: Character) -> None:
        pass

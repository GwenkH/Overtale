import pygame, random
from pygame import *


#Classes
class Character:

    def __init__(self, type: str, health: int) -> None:
        self.type = type
        self.health = health
        self.max_health = health
        self.shield = 10
        self.alive = True
        self.animations = []
        self.frame = 0
        self.action = 0 #0:idle, 1: attack, 2: block, 3: die
        self.last_update = pygame.time.get_ticks()
        
        #generate idle images
        action_list = []
        for image in range(4):
            img = pygame.transform.scale(
                pygame.image.load(f"{self.type}/idle_{image}.png"), (100, 125))
            action_list.append(img)
        self.animations.append(action_list)
        self.image = self.animations[self.action][self.frame]

        self.rect = self.image.get_rect()
        self.define_abilities()
        print(self.get_type())

    def get_type(self) -> None:
        return f"Generated {self.type}"

    def update(self) -> None: #Glenn -instance method modifying object data
        #Create animation
        animation_cd = 300
        #update image
        self.image = self.animations[self.action][self.frame]
        #time check
        if pygame.time.get_ticks() - self.last_update > animation_cd:
            self.last_update = pygame.time.get_ticks()
            self.frame += 1
        #animation loop reset
        if self.frame >= len(self.animations[self.action]):
            self.frame = 0
            
        
    def open_inventory(self) -> None:  #open menu for items
        pass

    def define_abilities(self) -> None: #Glenn-instance method
        if self.type == "knight":
            self.abilities = [Ability.heavy_hit, Ability.critical_stab]
        if self.type == "wizard":
            self.abilities = [
                Ability.special_ability, Ability.special_ability_2
            ]
        if self.type == "enemy":
            self.abilities = [
                Ability.enemy_basic_attack, Ability.enemy_special_attack
            ]

    def get_abilities(self) -> list:
        return(self.abilities)


class Ability:

    def __init__(self):
        pass

    def heavy_hit(self, target: Character) -> None: #Glenn-instance methods
        self.name = "Heavy Hit"
        self.damage = 40
        target.health = (target.health + target.shield) - self.damage

    def critical_stab(self, target: Character) -> None:
        self.name = "Critical Stab"
        self.damage = random.randint(20, 70)
        target.health = (target.health + target.shield) - self.damage

    def shield(self) -> None:  #reduce incoming damage from one enemy
        self.name = "Shield"
        self.shield += 20

    def special_ability(self, target: Character) -> None:
        pass

    def special_ability_2(self, target: Character) -> None:
        pass

    def enemy_basic_attack(self, target: Character) -> None:
        self.name = "Slash"
        self.damage = random.randint(40)
        target.health = (target.health + target.shield) - self.damage

    def enemy_special_attack(self, target: Character) -> None:
        self.name = "Piercing Strike"
        self.damage = random.randint(30,50)
        target.heatlh = target.health - self.damage
        
    def enemy_special_ability(self, target: Character) -> None:
        pass

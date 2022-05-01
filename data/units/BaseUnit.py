from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional, Union, Type

from data.classes.UnitClass import UnitClass
from data.equipment.armor import Armor
from data.equipment.weapons import Weapon

BASE_STAMINA_REGEN = 1


class BaseUnit(ABC):
    name: str
    char_class: UnitClass
    hit_points: float
    stamina_points: float
    weapon: Weapon
    armor: Armor
    used_skill_in_combat: bool

    def __init__(self, char_class: Type[UnitClass], weapon: Weapon, armor: Armor, name: str):
        self.name = name
        self.char_class = char_class
        self.hit_points = self.char_class.max_health
        self.stamina_points = self.char_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self.used_skill_in_combat = False

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def equip_armor(self, armor: Armor):
        self.armor = armor

    @property
    def total_armor(self):
        if self.stamina_points < self.armor.stamina_per_turn:
            return 0
        return self.armor.defence * self.char_class.armor

    def _hit(self, target: BaseUnit) -> Optional[str]:
        if self.stamina_points < self.weapon.stamina_per_hit:
            result = f"{self.name} попытался использовать {self.weapon.name}, " \
                     f"но у него не хватило выносливости."
            return result

        dmg = self.weapon.damage * self.char_class.attack
        total_damage = round(dmg - target.total_armor, 1)

        self.stamina_points -= self.weapon.stamina_per_hit
        # target.stamina_points -= target.armor.stamina_per_turn # Возможность терять выносливость про ударе
        if target.stamina_points < 0:
            target.stamina_points = 0

        if total_damage < 0:
            result = f"{self.name}, используя {self.weapon.name}, наносит удар, " \
                     f"но {target.armor.name} соперника его останавливает."
            return result

        target.suffer_damage(total_damage)
        result = f"{self.name}, используя {self.weapon.name}, пробивает {target.armor.name} " \
                 f"соперника и наносит {total_damage} урона."
        return result

    def suffer_damage(self, damage: float):
        self.hit_points = round(self.hit_points - damage, 1)
        if self.hit_points < 0:
            self.hit_points = 0

    def use_skill(self, target: BaseUnit) -> str:
        if self.stamina_points < self.char_class.skill.stamina_cost:
            return f"{self.name} попытался использовать {self.char_class.skill.name}, но у него не хватило выносливости."
        if self.used_skill_in_combat:
            return f"Навык уже использован."
        self.used_skill_in_combat = True
        dmg = round(self.char_class.skill.damage, 1)

        target.suffer_damage(dmg)

        return f"{self.name} использует {self.char_class.skill.name} и наносит {dmg} урона сопернику."


    def regenerate_stamina(self):
        regen_stamina = round(BASE_STAMINA_REGEN * self.char_class.stamina, 1)
        self.stamina_points = round(self.stamina_points + regen_stamina, 1)
        self.stamina_points = self.stamina_points if self.stamina_points <= self.char_class.max_stamina \
            else self.char_class.max_stamina


    @abstractmethod
    def hit(self, target: BaseUnit) -> Optional[float]:
        pass


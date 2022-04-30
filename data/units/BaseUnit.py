from dataclasses import dataclass
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

from data.classes.UnitClass import UnitClass
from data.equipment.armor import Armor
from data.equipment.weapons import Weapon

BASE_STAMINA_REGEN = 1

@dataclass
class BaseUnit(ABC):
#     - имя персонажа,
# - класс персонажа (объект, Воин или Вор),
# - очки здоровья,
# - очки выносливости,
# - оружие,
# - броня,
# - использован ли скил в бою
    name: str
    char_class: UnitClass
    hit_points: float
    stamina_points: float
    weapon: Weapon
    armor: Armor
    used_skill_in_combat: bool # ?

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def equip_armor(self, armor: Armor):
        self.armor = armor

    @property
    def total_armor(self):
        if self.stamina_points < self.armor.stamina_per_turn:
            return 0
        return self.armor.defence * self.char_class.armor

    def _hit(self, target: BaseUnit) -> Optional[float]:
        if self.stamina_points < self.weapon.stamina_per_hit:
            return None

        dmg = self.weapon.damage * self.char_class.attack
        total_damage = dmg - target.total_armor
        if total_damage < 0:
            return 0
        self.stamina_points -= self.weapon.stamina_per_hit
        return total_damage

    def suffer_damage(self, damage: float):
        self.hit_points -= damage
        if self.hit_points < 0:
            self.hit_points = 0

    def use_skill(self) -> Optional[float]:
        if self.stamina_points < self.char_class.skill.stamina_cost:
            return None
        self.used_skill_in_combat = True
        return round(self.char_class.skill.damage, 1)

    def regenerate_stamina(self):
        regen_stamina = BASE_STAMINA_REGEN * self.char_class.stamina
        # if regen_stamina + self.stamina_points < self.char_class.max_stamina:
        #     self.stamina_points += regen_stamina
        # else:
        #     self.stamina_points = self.char_class.max_stamina
        self.stamina_points += regen_stamina
        self.stamina_points = self.stamina_points if self.stamina_points <= self.char_class.max_stamina \
            else self.char_class.max_stamina


    @abstractmethod
    def hit(self, target: BaseUnit) -> Optional[float]:
        pass


from dataclasses import dataclass
from typing import List

from data.equipment.armor.Armor import Armor
from data.equipment.weapons.Weapon import Weapon


@dataclass
class EquipmentData():

    weapons: List[Weapon]
    armor: List[Armor]

    def get_weapon(self, w_name) -> Weapon:
        for weapon in self.weapons:
            if weapon.name == w_name:
                return weapon

        return RuntimeError

    def get_armor(self, a_name) -> Armor:
        for armor in self.armor:
            if armor.name == a_name:
                return armor

        return RuntimeError

    @property
    def weapon_names(self) -> List[str]:
        return [ w.name for w in self.weapons ]

    @property
    def armor_names(self) -> List[str]:
        return [ a.name for a in self.armor ]


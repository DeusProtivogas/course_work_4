from dataclasses import dataclass
from data.classes.UnitClass import UnitClass

from data.skills.DefaultSkill import DefaultSkill, ferocious_kick


@dataclass
class WarriorClass(UnitClass):
    name: str = "Воин"
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack: float = 0.8
    stamina: float = 0.9
    armor: float = 1.2
    skill: DefaultSkill = ferocious_kick

# w = WarriorClass()
# print(w)
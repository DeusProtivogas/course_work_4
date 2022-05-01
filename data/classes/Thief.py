from dataclasses import dataclass
from data.classes.UnitClass import UnitClass

from data.skills.DefaultSkill import DefaultSkill, powerful_stab


@dataclass
class ThiefClass(UnitClass):
    name: str = "Вор"
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack: float = 1.5
    stamina: float = 1.2
    armor: float = 1.0
    skill: DefaultSkill = powerful_stab

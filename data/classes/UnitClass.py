from dataclasses import dataclass
from abc import ABC, abstractmethod
from data.skills import DefaultSkill

@dataclass
class UnitClass(ABC):
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: DefaultSkill

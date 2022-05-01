from dataclasses import dataclass
from random import uniform
from abc import ABC


@dataclass
class Weapon(ABC):
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)

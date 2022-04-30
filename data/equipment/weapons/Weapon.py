from dataclasses import dataclass
from random import uniform
from abc import ABC, abstractmethod

@dataclass
class Weapon(ABC):
#     - Название (name).
# - Минимальный урон (min_damage).
# - Максимальный урон (max_damage).
# - Количество затрачиваемой выносливости за удар (stamina_per_hit).
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    # def calculate_damage(self):
    #     return uniform(self.min_damage, self.max_damage)

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)




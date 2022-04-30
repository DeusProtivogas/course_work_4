from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


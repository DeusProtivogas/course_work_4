# - название класса,
# - наносимый урон,
# - требуемая выносливость.

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class DefaultSkill():
    name: str
    damage: float
    stamina_cost: float

    # @abstractmethod
    def skill_effect(self):
        pass

    def use(self, user, target):
        if user.stamina > self.stamina_cost:
            return self.skill_effect()
        else:
            return "Not enough stamina!"


ferocious_kick = DefaultSkill(name="пинок", damage=12, stamina_cost=6)

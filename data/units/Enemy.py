from data.units.BaseUnit import BaseUnit
from typing import Optional
from random import randint


class Enemy(BaseUnit):
    def hit(self, target: BaseUnit) -> Optional[float]:
        if (randint(0, 100) <= 10) and self.stamina_points >= self.char_class.skill.stamina_cost \
                and not self.used_skill_in_combat:
            self.use_skill()
        else:
            pass


    # def hit(self, target: BaseUnit) -> Optional[float]:
    #     return self._hit(target)
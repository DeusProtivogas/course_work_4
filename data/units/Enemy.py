from data.units.BaseUnit import BaseUnit
from random import randint


class Enemy(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        if (randint(0, 100) <= 10) and self.stamina_points >= self.char_class.skill.stamina_cost \
                and not self.used_skill_in_combat:
            res = self.use_skill(target=target)
        else:
            res = self._hit(target=target)
        return res

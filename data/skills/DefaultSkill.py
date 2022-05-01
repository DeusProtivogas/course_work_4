from dataclasses import dataclass


@dataclass
class DefaultSkill():
    name: str
    damage: float
    stamina_cost: float

    def skill_effect(self):
        return self.damage

    def use(self, user):
        if user.stamina > self.stamina_cost:
            return self.skill_effect()
        else:
            return "Not enough stamina!"


ferocious_kick = DefaultSkill(name="пинок", damage=12, stamina_cost=6)

powerful_stab = DefaultSkill(name="Мощный укол", damage=15, stamina_cost=5)


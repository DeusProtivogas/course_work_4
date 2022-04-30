from data.units.BaseUnit import BaseUnit
from typing import Optional


class Player(BaseUnit):
    # def _hit(self, target: BaseUnit) -> Optional[float]:
    #     pass

    def hit(self, target: BaseUnit) -> Optional[float]:
        return self._hit(target)
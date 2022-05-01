import json
import os

import marshmallow_dataclass
from typing import Union, Dict

from data.classes.Thief import ThiefClass
from data.classes.UnitClass import UnitClass
from data.classes.Warrior import WarriorClass
from data.equipment.EquipmentData import EquipmentData

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
EQUIPMENT_DIR: str = os.path.join(BASE_DIR, "equipment", "equipment.json")


def read_json(path: str, encoding: str = "utf-8") -> Union[dict, list]:
    try:
        with open(path, encoding=encoding) as f:
            return json.loads(f.read())
    except Exception:
        raise


def load_equip():
    try:
        return marshmallow_dataclass.class_schema(EquipmentData)().load(
            data=read_json(EQUIPMENT_DIR)
        )
    except Exception:
        raise


# Классы
classes_list: Dict[str, UnitClass] = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass,
}

import json
import os

import marshmallow_dataclass
from typing import Union
from data.equipment.EquipmentData import EquipmentData

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
EQUIPMENT_DIR: str = os.path.join(BASE_DIR, "equipment", "equipment.json")

# print(BASE_DIR)
# print(EQUIPMENT_DIR)

def read_json(path: str, encoding: str = "utf-8") -> Union[dict, list]:
    try:
        with open(path, encoding=encoding) as f:
            # txt = f.read()
            # print(txt)
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

# d = load_equip()
# print(type(d))
# print(d)


from dataclasses import dataclass, field
from typing import Any


@dataclass
class Field:

    current_uid = 0
    uid: int = field(init=False)
    # price: Any = None
    # weight: Any = None

    def __post_init__(self):
        print("Fields post_init")
        Field.current_uid += 1
        self.uid = Field.current_uid


@dataclass
class Record(Field):
    name: str = ""
    phone: list = field(default_factory=list)
    birthday: str = ""
    email: str = ""
    address: str = ""

    def __post_init__(self):
        super().__post_init__()
        print("Record post_init")


v = Record('Rostyslav')
v2 = Record('Vasya')
# rec = Record(1, "Rostyslav", '+380504447755')
print(v)
print(v2)

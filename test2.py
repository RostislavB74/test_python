from dataclasses import dataclass, field
from typing import Any


@dataclass
class Goods:
    current_uid = 0
    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0.0
    weight: float = 0.0


v1 = Book(1000, 0.200, 'Rostyslav', 'test')
v = Book(title='Rostyslav', author='test', price=1000, weight=0.200)
print(v1)

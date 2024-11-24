from dataclasses import dataclass
from enum import Enum


class STATUS(Enum):
    stock = "В наличии"
    issued = "Выдана"


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: STATUS

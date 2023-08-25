from dataclasses import dataclass, asdict
from typing import List
from src.domain.entity.fields import Fields


@dataclass
class Category:
    id: int
    name: str
    fields: List[Fields] = None
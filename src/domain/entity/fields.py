from dataclasses import dataclass, asdict



@dataclass
class Fields:
    id: int
    name: str
    type_field: str
    category_id: int
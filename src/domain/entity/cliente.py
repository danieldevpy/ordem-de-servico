from dataclasses import dataclass, asdict


@dataclass
class Cliente:
    id: int
    name: str
    cel: str
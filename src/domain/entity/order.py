from dataclasses import dataclass


@dataclass
class Order:
    id: int
    data_json: str
    status: bool
    date: str
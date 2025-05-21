
from dataclasses import dataclass
from datetime import datetime

@dataclass
class StockLog:
    timestamp: datetime
    color: str
    model: str
    movement: str
    quantity: int
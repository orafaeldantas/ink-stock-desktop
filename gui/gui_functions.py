
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from dataclasses import dataclass
from services.stock_service import list_colors_by_model, update_quantity


@dataclass
class ButtonAction:
    entry: ctk.CTkEntry
    id: int = 0
    id_models: int = 0

    def get_value(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return 0
        
    def set_value(self, value: int):
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(value))

    def increase(self):
        value = self.get_value()
        self.set_value(min(value + 1, 100))

    def decrement(self):
        value = self.get_value()
        self.set_value(max(value - 1, 0))

    def output(self, id_models, id):
        actualy = get_paint_quantity_button(id_models, id)
        if self.get_value() > actualy:
            ...
        else:            
            update_quantity((actualy+self.get_value()), id)
            
            


def get_paint_quantity(id_models, id):
    color_amount = list_colors_by_model(id_models, id)
    color_amount = color_amount if color_amount is not None else 0
    return f"{color_amount[0][0]:03d}"

def get_paint_quantity_button(id_models, id):
    color_amount = list_colors_by_model(id_models, id)
    color_amount = color_amount if color_amount is not None else 0
    return color_amount[0][0]
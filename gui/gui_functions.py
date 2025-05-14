
import customtkinter as ctk

from dataclasses import dataclass 

@dataclass
class ButtonAction:
    entry: ctk.CTkEntry

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

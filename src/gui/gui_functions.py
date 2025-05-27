
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from dataclasses import dataclass
from services.stock_service import list_colors_by_model, update_quantity, list_model, list_color
from services.log_service import save_log_entry
from services.log_model import StockLog
from datetime import datetime
import logging



@dataclass
class ButtonAction:
    entry: ctk.CTkEntry
    id: int = 0
    id_models: int = 0
    callback_update_label: callable = None

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

    def input(self, id_models, id):
        actualy = get_paint_quantity_button(id_models, id)
           
        update_quantity((actualy+self.get_value()), id)
        if self.callback_update_label:
            self.callback_update_label(get_paint_quantity(id_models, id))
        
    
    def output(self, id_models, id):
        print(f"[DEBUG] output() chamado - id_models: {id_models}, id: {id}")
        actualy = get_paint_quantity_button(id_models, id)
        quantity_to_remove = self.get_value()
        
        if quantity_to_remove > actualy:
            print(f"[WARNING] Tentativa de remover {quantity_to_remove}, mas só tem {actualy}")
            # Aqui você pode adicionar uma mensagem de erro para o usuário
            pass
        else:
            update_quantity((actualy - quantity_to_remove), id)
            if self.callback_update_label:
                self.callback_update_label(get_paint_quantity(id_models, id))
            
            try:
                model_name = list_model(id_models)
                color_name = list_color(id)
                
                log = StockLog(
                    timestamp=datetime.now(),
                    color=color_name[0][0],
                    model=model_name[0][0],
                    movement="Saída",
                    quantity=quantity_to_remove
                )
                save_log_entry(log)
                
                
            except Exception as e:
                print(f"[ERRO] Falha ao criar/salvar log: {e}")
                import traceback
                traceback.print_exc()            
            
                      
def get_paint_quantity(id_models, id):
    color_amount = list_colors_by_model(id_models, id)
    color_amount = color_amount if color_amount is not None else 0
    return f"{color_amount[0][0]:03d}"

def get_paint_quantity_button(id_models, id):
    color_amount = list_colors_by_model(id_models, id)
    color_amount = color_amount if color_amount is not None else 0
    return color_amount[0][0]



import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from konica_cian import konica_cian_layout
from konica_yellow import konica_yellow_layout


def create_main_window():
    ctk.set_appearance_mode("System")  # Opcional: "Light", "Dark", "System"
    ctk.set_default_color_theme("blue")  # Pode ser "green", "dark-blue", etc.

    
    app = ctk.CTk()
    app.geometry("1200x800")
    app.title("Layout em Aba")

    # Criar o Tabview (as abas)
    tabview = ctk.CTkTabview(master=app)   
    tabview.pack(padx=20, pady=20, fill="both", expand=True)

    # Tab Konica
    tab_konica = tabview.add("Konica")
    tab_konica.grid_rowconfigure((0, 1), weight=0)
    tab_konica.grid_columnconfigure(0, weight=1)
    center_frame_konica_cian = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_cian.grid(row=0, column=0, sticky="")
    center_frame_konica_yellow = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_yellow.grid(row=1, column=0, sticky="")

    # Tab DX
    tab_dx = tabview.add("DX")
    tab_dx.grid_rowconfigure(0, weight=1)
    tab_dx.grid_columnconfigure(0, weight=1)
    center_frame_dx = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx.grid(row=0, column=0, sticky="")

    

    for tab_button in tabview._segmented_button._buttons_dict.values():
        tab_button.configure(font=("Arial", 30))


    # === Konica ==

    #Cian
    konica_cian_layout(center_frame_konica_cian)

    #Yellow
    konica_yellow_layout(center_frame_konica_yellow)
    
    app.mainloop()


if __name__ == "__main__":
    create_main_window()


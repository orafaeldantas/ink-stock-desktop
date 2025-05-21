import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
import tkinter as tk 
from gui.tab_konica import konica_cian_layout, konica_black_layout, konica_magenta_layout, konica_yellow_layout
from gui.tab_dx import dx_cian_layout, dx_black_layout, dx_magenta_layout, dx_yellow_layout
from gui.tab_uv_rolo import uv_rolo_cian_layout, uv_rolo_black_layout, uv_rolo_magenta_layout, uv_rolo_yellow_layout
from gui.tab_uv_mesa import uv_mesa_cian_layout, uv_mesa_black_layout, uv_mesa_magenta_layout, uv_mesa_yellow_layout

def center_window(app, width, height):
    app.update_idletasks()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    app.geometry(f"{width}x{height}+{x}+{y}")

def create_main_window():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")  

    
    app = ctk.CTk()

    window_width = 1200
    window_height = 900

    center_window(app, window_width, window_height)

    app.resizable(False, False)
    app.title("Tinta PeP")

    # Criar o Tabview (as abas)
    tabview = ctk.CTkTabview(master=app)   
    tabview.pack(padx=20, pady=20, fill="both", expand=True)

    # Tab Konica
    tab_konica = tabview.add("Konica")
    tab_konica.grid_rowconfigure((0, 3), weight=0)
    tab_konica.grid_columnconfigure(0, weight=1)

    center_frame_konica_cian = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_cian.grid(row=0, column=0, sticky="", pady=30)

    center_frame_konica_yellow = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_yellow.grid(row=1, column=0, sticky="", pady=30)

    center_frame_konica_magenta = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_magenta.grid(row=2, column=0, sticky="", pady=30)

    center_frame_konica_black = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica_black.grid(row=3, column=0, sticky="", pady=30)

    # Tab DX
    tab_dx = tabview.add("DX")
    tab_dx.grid_rowconfigure((0, 3), weight=0)
    tab_dx.grid_columnconfigure(0, weight=1)

    center_frame_dx_cian = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx_cian.grid(row=0, column=0, sticky="", pady=30)

    center_frame_dx_yellow = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx_yellow.grid(row=1, column=0, sticky="", pady=30)

    center_frame_dx_magenta = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx_magenta.grid(row=2, column=0, sticky="", pady=30)

    center_frame_dx_black = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx_black.grid(row=3, column=0, sticky="", pady=30)

    # Tab UV rolo
    tab_uv_rolo = tabview.add("UV Rolo")
    tab_uv_rolo.grid_rowconfigure((0, 3), weight=0)
    tab_uv_rolo.grid_columnconfigure(0, weight=1)

    center_frame_uv_rolo_cian = ctk.CTkFrame(tab_uv_rolo, fg_color='transparent')
    center_frame_uv_rolo_cian.grid(row=0, column=0, sticky="", pady=30)

    center_frame_uv_rolo_yellow = ctk.CTkFrame(tab_uv_rolo, fg_color='transparent')
    center_frame_uv_rolo_yellow.grid(row=1, column=0, sticky="", pady=30)

    center_frame_uv_rolo_magenta = ctk.CTkFrame(tab_uv_rolo, fg_color='transparent')
    center_frame_uv_rolo_magenta.grid(row=2, column=0, sticky="", pady=30)

    center_frame_uv_rolo_black = ctk.CTkFrame(tab_uv_rolo, fg_color='transparent')
    center_frame_uv_rolo_black.grid(row=3, column=0, sticky="", pady=30)

    # Tab UV mesa
    tab_uv_mesa = tabview.add("UV Mesa")
    tab_uv_mesa.grid_rowconfigure((0, 3), weight=0)
    tab_uv_mesa.grid_columnconfigure(0, weight=1)

    center_frame_uv_mesa_cian = ctk.CTkFrame(tab_uv_mesa, fg_color='transparent')
    center_frame_uv_mesa_cian.grid(row=0, column=0, sticky="", pady=30)

    center_frame_uv_mesa_yellow = ctk.CTkFrame(tab_uv_mesa, fg_color='transparent')
    center_frame_uv_mesa_yellow.grid(row=1, column=0, sticky="", pady=30)

    center_frame_uv_mesa_magenta = ctk.CTkFrame(tab_uv_mesa, fg_color='transparent')
    center_frame_uv_mesa_magenta.grid(row=2, column=0, sticky="", pady=30)

    center_frame_uv_mesa_black = ctk.CTkFrame(tab_uv_mesa, fg_color='transparent')
    center_frame_uv_mesa_black.grid(row=3, column=0, sticky="", pady=30)

    

    for tab_button in tabview._segmented_button._buttons_dict.values():
        tab_button.configure(font=("Arial", 30))


    # === Konica ==

    #Cian
    konica_cian_layout(center_frame_konica_cian)

    #Yellow
    konica_yellow_layout(center_frame_konica_yellow)

    #Magenta
    konica_magenta_layout(center_frame_konica_magenta)

    #Black
    konica_black_layout(center_frame_konica_black)

    # === DX ==

    #Cian
    dx_cian_layout(center_frame_dx_cian)

    #Yellow
    dx_yellow_layout(center_frame_dx_yellow)

    #Magenta
    dx_magenta_layout(center_frame_dx_magenta)

    #Black
    dx_black_layout(center_frame_dx_black)

        # === UV Rolo ==

    #Cian
    uv_rolo_cian_layout(center_frame_uv_rolo_cian)

    #Yellow
    uv_rolo_yellow_layout(center_frame_uv_rolo_yellow)

    #Magenta
    uv_rolo_magenta_layout(center_frame_uv_rolo_magenta)

    #Black
    uv_rolo_black_layout(center_frame_uv_rolo_black)

        # === UV Mesa ==

    #Cian
    uv_mesa_cian_layout(center_frame_uv_mesa_cian)

    #Yellow
    uv_mesa_yellow_layout(center_frame_uv_mesa_yellow)

    #Magenta
    uv_mesa_magenta_layout(center_frame_uv_mesa_magenta)

    #Black
    uv_mesa_black_layout(center_frame_uv_mesa_black)
    
    app.mainloop()


if __name__ == "__main__":
    create_main_window()


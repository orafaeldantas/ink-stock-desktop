import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk


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
    tab_konica.grid_rowconfigure(0, weight=1)
    tab_konica.grid_columnconfigure(0, weight=1)
    center_frame_konica = ctk.CTkFrame(tab_konica, fg_color='transparent')
    center_frame_konica.grid(row=0, column=0, sticky="")

    tab_dx = tabview.add("DX")
    tab_dx.grid_rowconfigure(0, weight=1)
    tab_dx.grid_columnconfigure(0, weight=1)
    center_frame_dx = ctk.CTkFrame(tab_dx, fg_color='transparent')
    center_frame_dx.grid(row=0, column=0, sticky="")

    

    for tab_button in tabview._segmented_button._buttons_dict.values():
        tab_button.configure(font=("Arial", 30))


    #Konica layout
    circle_canvas = ctk.CTkCanvas(center_frame_konica, width=60, height=60, bg="white", highlightthickness=0)
    circle_canvas.grid(row=0, column=0, padx=10)
    circle_canvas.create_oval(10, 10, 50, 50, fill="#3B82F6")

    label_konica_cian = ctk.CTkLabel(center_frame_konica, text="00", font=ctk.CTkFont(size=100, weight="bold"))
    label_konica_cian.grid(row=0, column=1, padx=30)

    button_frame_konica = ctk.CTkFrame(center_frame_konica, fg_color="transparent")
    button_frame_konica.grid(row=0, column=2, padx=10, sticky="e")    

    btn1 = ctk.CTkButton(button_frame_konica, text="Entrada 1")
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica, text="Saída 1")
    btn2.grid(row=0, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica, text="Entrada 2")
    btn3.grid(row=1, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica, text="Saída 2")
    btn4.grid(row=1, column=1, padx=5, pady=5)
    
    app.mainloop()


if __name__ == "__main__":
    create_main_window()


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk


def create_main_window():
    ctk.set_appearance_mode("System")  # Opcional: "Light", "Dark", "System"
    ctk.set_default_color_theme("blue")  # Pode ser "green", "dark-blue", etc.

    window = ctk.CTk()
    window.title("Abas com CustomTkinter")
    window.geometry("1200x800")

    # Criar o Tabview (as abas)
    tabview = ctk.CTkTabview(master=window)   
    tabview.pack(padx=20, pady=20, fill="both", expand=True)

    # Adicionar abas
    tabview.add("Konica")
    tabview.add("DX")    
    tabview.add("UV Rolo")
    tabview.add("UV Mesa")
    tabview.add("Configurações")

    for tab_button in tabview._segmented_button._buttons_dict.values():
        tab_button.configure(font=("Arial", 30))

    # Pegar referências para cada aba
    tabKonica = tabview.tab("Konica")
    tabDX = tabview.tab("DX")
    tabUVRolo = tabview.tab("UV Rolo")
    tabUVMesa = tabview.tab("UV Mesa")
    config = tabview.tab("Configurações")

    # Adicionar conteúdo em cada aba
    labelKonica = ctk.CTkLabel(tabKonica, text="Konica")
    labelKonica.pack(pady=10)

    labelDX = ctk.CTkLabel(tabDX, text="DX")
    labelDX.pack(pady=10)

    labelUVRolo = ctk.CTkLabel(tabUVRolo, text="UV Rolo")
    labelUVRolo.pack(pady=10)

    labelUVMesa = ctk.CTkLabel(tabUVMesa, text="UV Mesa")
    labelUVMesa.pack(pady=10)


    #Konica layout
    stockValueKonica = ctk.CTkLabel(tabKonica, text="00", font=ctk.CTkFont(size=128))
    stockValueKonica.pack(pady=10)
    
    window.mainloop()


if __name__ == "__main__":
    create_main_window()


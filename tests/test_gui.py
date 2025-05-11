import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk

def create_main_window():
    # Criar a janela principal
    window = ctk.CTk()
    window.title("Minha Janela CustomTkinter")
    window.geometry("1200x800")

    # Adicionar um botão simples
    def on_button_click():
        print("Botão clicado!")

    button = ctk.CTkButton(window, text="Clique aqui", command=on_button_click)
    button.pack(pady=20)

    # Adicionar um campo de entrada de texto
    entry = ctk.CTkEntry(window)
    entry.pack(pady=20)

    # Adicionar um label
    label = ctk.CTkLabel(window, text="Texto simples no Label")
    label.pack(pady=20)

    # Exibir a janela
    window.mainloop()

if __name__ == "__main__":
    create_main_window()


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk

# Inicialização
ctk.set_appearance_mode("light")  # Ou "dark"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x200")
app.title("Layout com Círculo, Label e Botões")

# Frame principal
main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)
main_frame.grid_columnconfigure(1, weight=1)

# 🔵 Círculo à esquerda (simulado com CTkCanvas)
circle_canvas = ctk.CTkCanvas(main_frame, width=60, height=60, bg="white", highlightthickness=0)
circle_canvas.grid(row=0, column=0, padx=10)
circle_canvas.create_oval(10, 10, 50, 50, fill="#3B82F6")  # Azul

# 🏷️ Label no centro
label = ctk.CTkLabel(
    main_frame,
    text="Modelo Konica",
    font=ctk.CTkFont(size=24, weight="bold"),
    text_color="black"
)
label.grid(row=0, column=1, padx=30)

# 🔘 Botões à direita em pares
buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
buttons_frame.grid(row=0, column=2, padx=10)

btn1 = ctk.CTkButton(buttons_frame, text="Entrada 1", font=ctk.CTkFont(size=14))
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = ctk.CTkButton(buttons_frame, text="Saída 1", font=ctk.CTkFont(size=14))
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = ctk.CTkButton(buttons_frame, text="Entrada 2", font=ctk.CTkFont(size=14))
btn3.grid(row=1, column=0, padx=5, pady=5)

btn4 = ctk.CTkButton(buttons_frame, text="Saída 2", font=ctk.CTkFont(size=14))
btn4.grid(row=1, column=1, padx=5, pady=5)

# Iniciar o app
app.mainloop()

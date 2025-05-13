import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk

# Inicialização
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x250")
app.title("Layout em Aba")

# Tabview
tabview = ctk.CTkTabview(app, width=650, height=200)
tabview.pack(padx=20, pady=20)

# Criar uma aba chamada "Konica"
tab_konica = tabview.add("Konica")

# Configurar layout interno com grid
tab_konica.grid_columnconfigure(1, weight=1)

# 🎯 Círculo à esquerda
circle_canvas = ctk.CTkCanvas(tab_konica, width=60, height=60, bg="white", highlightthickness=0)
circle_canvas.grid(row=0, column=0, padx=10)
circle_canvas.create_oval(10, 10, 50, 50, fill="#3B82F6")  # Azul

# 🏷️ Label no centro
label = ctk.CTkLabel(tab_konica, text="Modelo Konica", font=ctk.CTkFont(size=22, weight="bold"))
label.grid(row=0, column=1, padx=30)

# 🔘 Botões à direita (em par)
button_frame = ctk.CTkFrame(tab_konica, fg_color="transparent")
button_frame.grid(row=0, column=2, padx=10)

btn1 = ctk.CTkButton(button_frame, text="Entrada 1")
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = ctk.CTkButton(button_frame, text="Saída 1")
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = ctk.CTkButton(button_frame, text="Entrada 2")
btn3.grid(row=1, column=0, padx=5, pady=5)

btn4 = ctk.CTkButton(button_frame, text="Saída 2")
btn4.grid(row=1, column=1, padx=5, pady=5)

# Iniciar app
app.mainloop()

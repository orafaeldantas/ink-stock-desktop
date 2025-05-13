
import customtkinter as ctk

def konica_yellow_layout(center_frame_konica_yellow):
    circle_canvas_yellow = ctk.CTkCanvas(center_frame_konica_yellow, width=60, height=60, bg="white", highlightthickness=0)
    circle_canvas_yellow.grid(row=0, column=0, padx=10)
    circle_canvas_yellow.create_oval(10, 10, 50, 50, fill="#00FF00")

    label_konica_yellow = ctk.CTkLabel(center_frame_konica_yellow, text="00", font=ctk.CTkFont(size=100, weight="bold"))
    label_konica_yellow.grid(row=0, column=1, padx=30)

    button_frame_konica_yellow = ctk.CTkFrame(center_frame_konica_yellow, fg_color="transparent")
    button_frame_konica_yellow.grid(row=0, column=2, padx=10, sticky="e")    

    btn1 = ctk.CTkButton(button_frame_konica_yellow, text="Entrada 1")
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_yellow, text="Saída 1")
    btn2.grid(row=0, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_yellow, text="Entrada 2")
    btn3.grid(row=1, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_yellow, text="Saída 2")
    btn4.grid(row=1, column=1, padx=5, pady=5)

import customtkinter as ctk


def konica_black_layout(center_frame_konica_cian):
    circle_canvas_black = ctk.CTkCanvas(center_frame_konica_cian, width=60, height=60, bg="white", highlightthickness=0)
    circle_canvas_black.grid(row=0, column=0, padx=10)
    circle_canvas_black.create_oval(10, 10, 50, 50, fill="#000000")

    label_konica_black = ctk.CTkLabel(center_frame_konica_cian, text="00", font=ctk.CTkFont(size=100, weight="bold"))
    label_konica_black.grid(row=0, column=1, padx=30)

    button_frame_konica_black= ctk.CTkFrame(center_frame_konica_cian, fg_color="transparent")
    button_frame_konica_black.grid(row=0, column=2, padx=10, sticky="e")    

    btn1 = ctk.CTkButton(button_frame_konica_black, text="Entrada 1")
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_black, text="Saída 1")
    btn2.grid(row=0, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_black, text="Entrada 2")
    btn3.grid(row=1, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_black, text="Saída 2")
    btn4.grid(row=1, column=1, padx=5, pady=5)


def konica_cian_layout(center_frame_konica_cian):
    circle_canvas_cian = ctk.CTkCanvas(center_frame_konica_cian, width=60, height=60, bg="white", highlightthickness=0)
    circle_canvas_cian.grid(row=0, column=0, padx=10)
    circle_canvas_cian.create_oval(10, 10, 50, 50, fill="#3B82F6")

    label_konica_cian = ctk.CTkLabel(center_frame_konica_cian, text="00", font=ctk.CTkFont(size=100, weight="bold"))
    label_konica_cian.grid(row=0, column=1, padx=30)

    button_frame_konica_cian = ctk.CTkFrame(center_frame_konica_cian, fg_color="transparent")
    button_frame_konica_cian.grid(row=0, column=2, padx=10, sticky="e")    

    btn1 = ctk.CTkButton(button_frame_konica_cian, text="Entrada 1")
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_cian, text="Saída 1")
    btn2.grid(row=0, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_cian, text="Entrada 2")
    btn3.grid(row=1, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_cian, text="Saída 2")
    btn4.grid(row=1, column=1, padx=5, pady=5)


def konica_magenta_layout(center_frame_konica_cian):
    circle_canvas_magenta = ctk.CTkCanvas(center_frame_konica_cian, width=60, height=60, bg="white", highlightthickness=0)
    circle_canvas_magenta.grid(row=0, column=0, padx=10)
    circle_canvas_magenta.create_oval(10, 10, 50, 50, fill="#0000FF")

    label_konica_magenta = ctk.CTkLabel(center_frame_konica_cian, text="00", font=ctk.CTkFont(size=100, weight="bold"))
    label_konica_magenta.grid(row=0, column=1, padx=30)

    button_frame_konica_magenta = ctk.CTkFrame(center_frame_konica_cian, fg_color="transparent")
    button_frame_konica_magenta.grid(row=0, column=2, padx=10, sticky="e")    

    btn1 = ctk.CTkButton(button_frame_konica_magenta, text="Entrada 1")
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_magenta, text="Saída 1")
    btn2.grid(row=0, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_magenta, text="Entrada 2")
    btn3.grid(row=1, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_magenta, text="Saída 2")
    btn4.grid(row=1, column=1, padx=5, pady=5)


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
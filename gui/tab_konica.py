
import customtkinter as ctk
from gui_functions import ButtonAction, get_paint_quantity, get_paint_quantity_button


font_label_stock = 90

def konica_black_layout(center_frame_konica_black):
    circle_canvas_black = ctk.CTkCanvas(center_frame_konica_black, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_black.grid(row=0, column=0, padx=10)
    circle_canvas_black.create_oval(5, 5, 65, 65, fill="#000000")

    label_konica_black = ctk.CTkLabel(center_frame_konica_black, text="00", font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_konica_black.grid(row=0, column=1, padx=30)

    button_frame_konica_black= ctk.CTkFrame(center_frame_konica_black, fg_color="transparent")
    button_frame_konica_black.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_konica_black, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    btn1 = ctk.CTkButton(button_frame_konica_black, text="Entrada 1")
    btn1.grid(row=1, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_black, text="Saída 1")
    btn2.grid(row=1, column=1, padx=5, pady=5)


    btn3 = ctk.CTkButton(button_frame_konica_black, text="Entrada 2")
    btn3.grid(row=2, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_black, text="Saída 2")
    btn4.grid(row=2, column=1, padx=5, pady=5)


def konica_cian_layout(center_frame_konica_cian):
    circle_canvas_cian = ctk.CTkCanvas(center_frame_konica_cian, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_cian.grid(row=0, column=0, padx=10)
    circle_canvas_cian.create_oval(5, 5, 65, 65, fill="#00BFFF")

    label_konica_cian = ctk.CTkLabel(center_frame_konica_cian, text="00", font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_konica_cian.grid(row=0, column=1, padx=30)

    button_frame_konica_cian = ctk.CTkFrame(center_frame_konica_cian, fg_color="transparent")
    button_frame_konica_cian.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_konica_cian, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    btn1 = ctk.CTkButton(button_frame_konica_cian, text="Entrada 1")
    btn1.grid(row=1, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_cian, text="Saída 1")
    btn2.grid(row=1, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_cian, text="Entrada 2")
    btn3.grid(row=2, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_cian, text="Saída 2")
    btn4.grid(row=2, column=1, padx=5, pady=5)


def konica_magenta_layout(center_frame_konica_magenta):
    circle_canvas_magenta = ctk.CTkCanvas(center_frame_konica_magenta, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_magenta.grid(row=0, column=0, padx=10)
    circle_canvas_magenta.create_oval(5, 5, 65, 65, fill="#8B008B")

    label_konica_magenta = ctk.CTkLabel(center_frame_konica_magenta, text="00", font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_konica_magenta.grid(row=0, column=1, padx=30)

    button_frame_konica_magenta = ctk.CTkFrame(center_frame_konica_magenta, fg_color="transparent")
    button_frame_konica_magenta.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_konica_magenta, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    btn1 = ctk.CTkButton(button_frame_konica_magenta, text="Entrada 1")
    btn1.grid(row=1, column=0, padx=5, pady=5)

    btn2 = ctk.CTkButton(button_frame_konica_magenta, text="Saída 1")
    btn2.grid(row=1, column=1, padx=5, pady=5)

    btn3 = ctk.CTkButton(button_frame_konica_magenta, text="Entrada 2")
    btn3.grid(row=2, column=0, padx=5, pady=5)

    btn4 = ctk.CTkButton(button_frame_konica_magenta, text="Saída 2")
    btn4.grid(row=2, column=1, padx=5, pady=5)


def konica_yellow_layout(center_frame_konica_yellow):
    circle_canvas_yellow = ctk.CTkCanvas(center_frame_konica_yellow, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_yellow.grid(row=0, column=0, padx=10)
    circle_canvas_yellow.create_oval(5, 5, 65, 65, fill="#FFFF00")

    label_konica_yellow = ctk.CTkLabel(center_frame_konica_yellow, text=get_paint_quantity_button(1, 1), font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_konica_yellow.grid(row=0, column=1, padx=30)

    button_frame_konica_yellow = ctk.CTkFrame(center_frame_konica_yellow, fg_color="transparent")
    button_frame_konica_yellow.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_konica_yellow, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    button_action = ButtonAction(entry=quantity_entry)

    btn_increase = ctk.CTkButton(button_frame_konica_yellow, text="+", font=ctk.CTkFont(size=18), command=button_action.increase)
    btn_increase.grid(row=1, column=0, padx=5, pady=5)   

    btn_decrease = ctk.CTkButton(button_frame_konica_yellow, text="-", font=ctk.CTkFont(size=18), command=button_action.decrement)
    btn_decrease.grid(row=2, column=0, padx=5, pady=5)

    btn_input = ctk.CTkButton(button_frame_konica_yellow, text="Entrada", fg_color="#006400", font=ctk.CTkFont(size=18), command=lambda: button_action.output(1, 1))
    btn_input.grid(row=1, column=1, padx=5, pady=5)

    btn_output = ctk.CTkButton(button_frame_konica_yellow, text="Saída", fg_color="#8B0000", font=ctk.CTkFont(size=18))
    btn_output.grid(row=2, column=1, padx=5, pady=5)

import customtkinter as ctk
from gui.gui_functions import ButtonAction, get_paint_quantity


font_label_stock = 90

def dx_black_layout(center_frame_dx_black):
    circle_canvas_black = ctk.CTkCanvas(center_frame_dx_black, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_black.grid(row=0, column=0, padx=10)
    circle_canvas_black.create_oval(5, 5, 65, 65, fill="#000000")

    label_dx_black = ctk.CTkLabel(center_frame_dx_black, text=get_paint_quantity(2, 8), font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_dx_black.grid(row=0, column=1, padx=30)

    def update_label(new_text):
        label_dx_black.configure(text=new_text)

    button_frame_dx_black = ctk.CTkFrame(center_frame_dx_black, fg_color="transparent")
    button_frame_dx_black.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_dx_black, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    button_action = ButtonAction(entry=quantity_entry, callback_update_label=update_label)

    btn_increase = ctk.CTkButton(button_frame_dx_black, text="+", font=ctk.CTkFont(size=18), command=button_action.increase)
    btn_increase.grid(row=1, column=0, padx=5, pady=5)   

    btn_decrease = ctk.CTkButton(button_frame_dx_black, text="-", font=ctk.CTkFont(size=18), command=button_action.decrement)
    btn_decrease.grid(row=2, column=0, padx=5, pady=5)
    
    btn_input = ctk.CTkButton(
        button_frame_dx_black, 
        text="Entrada", 
        fg_color="#006400", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.input(2, 8),
        hover_color="#228B22"
    )
    btn_input.grid(row=1, column=1, padx=5, pady=5)

    btn_output = ctk.CTkButton(
        button_frame_dx_black, 
        text="Saída", fg_color="#8B0000", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.output(2, 8),
        hover_color="#9B111E"
    )
    btn_output.grid(row=2, column=1, padx=5, pady=5)


def dx_cian_layout(center_frame_dx_cian):
    circle_canvas_cian = ctk.CTkCanvas(center_frame_dx_cian, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_cian.grid(row=0, column=0, padx=10)
    circle_canvas_cian.create_oval(5, 5, 65, 65, fill="#00BFFF")

    label_dx_cian = ctk.CTkLabel(center_frame_dx_cian, text=get_paint_quantity(2, 7), font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_dx_cian.grid(row=0, column=1, padx=30)

    def update_label(new_text):
        label_dx_cian.configure(text=new_text)

    button_frame_dx_cian = ctk.CTkFrame(center_frame_dx_cian, fg_color="transparent")
    button_frame_dx_cian.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_dx_cian, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    button_action = ButtonAction(entry=quantity_entry, callback_update_label=update_label)

    btn_increase = ctk.CTkButton(button_frame_dx_cian, text="+", font=ctk.CTkFont(size=18), command=button_action.increase)
    btn_increase.grid(row=1, column=0, padx=5, pady=5)   

    btn_decrease = ctk.CTkButton(button_frame_dx_cian, text="-", font=ctk.CTkFont(size=18), command=button_action.decrement)
    btn_decrease.grid(row=2, column=0, padx=5, pady=5)
    
    btn_input = ctk.CTkButton(
        button_frame_dx_cian, 
        text="Entrada", 
        fg_color="#006400", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.input(2, 7),
        hover_color="#228B22"
    )
    btn_input.grid(row=1, column=1, padx=5, pady=5)

    btn_output = ctk.CTkButton(
        button_frame_dx_cian, 
        text="Saída", fg_color="#8B0000", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.output(2, 7),
        hover_color="#9B111E"
    )
    btn_output.grid(row=2, column=1, padx=5, pady=5)


def dx_magenta_layout(center_frame_dx_magenta):
    circle_canvas_magenta = ctk.CTkCanvas(center_frame_dx_magenta, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_magenta.grid(row=0, column=0, padx=10)
    circle_canvas_magenta.create_oval(5, 5, 65, 65, fill="#8B008B")

    label_dx_magenta = ctk.CTkLabel(center_frame_dx_magenta, text=get_paint_quantity(2, 6), font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_dx_magenta.grid(row=0, column=1, padx=30)

    def update_label(new_text):
        label_dx_magenta.configure(text=new_text)

    button_frame_dx_magenta = ctk.CTkFrame(center_frame_dx_magenta, fg_color="transparent")
    button_frame_dx_magenta.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_dx_magenta, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    button_action = ButtonAction(entry=quantity_entry, callback_update_label=update_label)

    btn_increase = ctk.CTkButton(button_frame_dx_magenta, text="+", font=ctk.CTkFont(size=18), command=button_action.increase)
    btn_increase.grid(row=1, column=0, padx=5, pady=5)   

    btn_decrease = ctk.CTkButton(button_frame_dx_magenta, text="-", font=ctk.CTkFont(size=18), command=button_action.decrement)
    btn_decrease.grid(row=2, column=0, padx=5, pady=5)
    
    btn_input = ctk.CTkButton(
        button_frame_dx_magenta, 
        text="Entrada", 
        fg_color="#006400", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.input(2, 6),
        hover_color="#228B22"
    )
    btn_input.grid(row=1, column=1, padx=5, pady=5)

    btn_output = ctk.CTkButton(
        button_frame_dx_magenta, 
        text="Saída", fg_color="#8B0000", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.output(2, 6),
        hover_color="#9B111E"
    )
    btn_output.grid(row=2, column=1, padx=5, pady=5)


def dx_yellow_layout(center_frame_dx_yellow):
    circle_canvas_yellow = ctk.CTkCanvas(center_frame_dx_yellow, width=70, height=70, bg="white", highlightthickness=0)
    circle_canvas_yellow.grid(row=0, column=0, padx=10)
    circle_canvas_yellow.create_oval(5, 5, 65, 65, fill="#FFFF00")

    label_dx_yellow = ctk.CTkLabel(center_frame_dx_yellow, text=get_paint_quantity(2, 5), font=ctk.CTkFont(size=font_label_stock, weight="bold"))
    label_dx_yellow.grid(row=0, column=1, padx=30)

    def update_label(new_text):
        label_dx_yellow.configure(text=new_text)

    button_frame_dx_yellow = ctk.CTkFrame(center_frame_dx_yellow, fg_color="transparent")
    button_frame_dx_yellow.grid(row=0, column=2, padx=10, sticky="e")    

    quantity_entry = ctk.CTkEntry(button_frame_dx_yellow, placeholder_text="0", font=ctk.CTkFont(size=18), justify="center")
    quantity_entry.grid(row=0, column=0,columnspan=2, padx=10, pady=(5, 10), sticky="ew")

    button_action = ButtonAction(entry=quantity_entry, callback_update_label=update_label)

    btn_increase = ctk.CTkButton(button_frame_dx_yellow, text="+", font=ctk.CTkFont(size=18), command=button_action.increase)
    btn_increase.grid(row=1, column=0, padx=5, pady=5)   

    btn_decrease = ctk.CTkButton(button_frame_dx_yellow, text="-", font=ctk.CTkFont(size=18), command=button_action.decrement)
    btn_decrease.grid(row=2, column=0, padx=5, pady=5)
    
    btn_input = ctk.CTkButton(
        button_frame_dx_yellow, 
        text="Entrada", 
        fg_color="#006400", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.input(2, 5),
        hover_color="#228B22"
    )
    btn_input.grid(row=1, column=1, padx=5, pady=5)

    btn_output = ctk.CTkButton(
        button_frame_dx_yellow, 
        text="Saída", fg_color="#8B0000", 
        font=ctk.CTkFont(size=18), 
        command=lambda: button_action.output(2, 5),
        hover_color="#9B111E"             
    )
    btn_output.grid(row=2, column=1, padx=5, pady=5)
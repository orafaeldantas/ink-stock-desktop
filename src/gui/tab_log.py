
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from services.log_service import load_logs


def log_tab_layout(center_frame_log_tab):

    for widget in center_frame_log_tab.winfo_children():
        widget.destroy()

    log_textbox = ctk.CTkTextbox(center_frame_log_tab, width=750, height=550)
    log_textbox.pack(padx=10, pady=10)

    logs = load_logs()
    log_textbox.delete("1.0", "end")  # limpa antes de carregar
    if logs:
        for i, log in enumerate(logs, start=1):
            log_textbox.insert("end", f"--- Log {i} ---\n")
            for key, value in log.items():
                log_textbox.insert("end", f"{key}: {value}\n")
            log_textbox.insert("end", "\n")
        log_textbox.see(ctk.END)
    else:
        log_textbox.insert("end", "Nenhum log encontrado.")
    


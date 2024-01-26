# Copyright (c) 2024 Logan Dhillon

import tkinter as tk
from tkextrafont import Font

def check_answer():
    if prompt == text_field.get():
        prompt_label.config(text="WOOHOO")

prompt = "the quick brown fox jumps over the lazy dog"

window = tk.Tk()
window.title("SGA Trainer")

# init SGA font
sga_font = Font(file="resources/sga.ttf", family="Enchantment Proper")

prompt_label = tk.Label(window, text=prompt, font=sga_font)
text_field = tk.Entry(window, width=64)

tk.Label(window, text="What does this say?", font=("", 16)).pack(pady=10, padx=10)
prompt_label.pack(pady=10, padx=10)
text_field.pack(pady=10, padx=10)
tk.Button(window, text="Submit", command=check_answer).pack(pady=10)

window.mainloop()
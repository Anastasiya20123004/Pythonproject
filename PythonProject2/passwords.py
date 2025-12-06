from customtkinter import *
from random import choice

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS/*-+=_!&@#^()"
    result = ""
    for i in range(8):
        result += "".join(choice(chars))
    password_entry.delete(0, "end")
    password_entry.insert(0, result)

set_default_color_theme("blue")

window = CTk()
window.geometry("300*120")
window.resizable(False, False)
window.title("Generate password")

password_entry = CTkEntry(window, width = 200)
password_entry.pack(pady = 10)

CTkButton(window, text = "Generate", command = generate_password).pack()

window.mainloop()
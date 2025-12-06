from customtkinter import *
from random import randint

window = CTk()
window.geometry('400x300')


def buttton_adaptive():
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    btn.configure(width=window_width - 100, height=window_height - 120)

    window.after(25, buttton_adaptive)


lable = CTkLabel(window, text="TEXT")
lable.place(x=50, y=40)
btn = CTkButton(window, text='', width=300, height=100)
btn.place(x=50, y=40)
buttton_adaptive()

window.mainloop()
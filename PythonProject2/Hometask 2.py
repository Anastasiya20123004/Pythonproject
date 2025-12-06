from customtkinter import *

window = CTk()
window.geometry("400 * 300")
window.title("First app")
window.configure(fg_color = "lightyellow")

font = ("Times", 33, "bold")
label = CTkLabel(window, text = "Hello Logika!", text_color = "blue",  font = font, height = 150, width = 400)
label.pack()

window.mainloop()
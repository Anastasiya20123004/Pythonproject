from customtkinter import *

window = CTk()
window.geometry("400 * 400")
window.title("Task 2")

text = CTkTextbox(window, height = 280, width = 380)
text.pack(pady = 10)
entry = CTkEntry(window, width = 380)
entry.pack(pady = 10)
font = ("Calibri", 20, "normal")
button = CTkButton(window, text = "Клік", font = font, width = 380)
button.pack(pady = 5)

window.mainloop()
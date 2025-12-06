from customtkinter import *

window = CTk()
window.geometry("500x500")
window.configure(fg_color = "white")
window.title("Clicker")

font = ("Arial", 30, "bold")
text = CTkLabel(window, text = "Тут буде твій рахунок", font = font, text_color = "black", width = 500, height = 200)
text.pack()
button = CTkButton(window, text = "Click", font = font, width = 480, height = 250)
button.pack()

window.mainloop()
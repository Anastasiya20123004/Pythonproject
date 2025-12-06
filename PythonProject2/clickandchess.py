from customtkinter import *

window = CTk()
window.geometry("400*400")
window.title("Teto clicker")
font = ("Arial", 30, "bold")
score = 0
score_text = CTkLabel(window, text = score, font = font)
score_text.pack(pady = 15)

def click():
    global score
    score += 1
    score_text.configure(text = score)

click_btn = CTkButton(window, text ="Click", command = click, width = 300, height = 300, font = font)
click_btn.pack()

window.mainloop()
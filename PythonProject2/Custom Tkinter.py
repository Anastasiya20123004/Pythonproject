from customtkinter import *
window = CTk()
window.geometry("400 * 400")
window.title("Перший чат з CTk")
window.configure(fg_color = "lightblue")
text = CTkLabel(window, text = "Введіть текст", fg_color = "lightyellow", width = 400, height = 200, font = ("Arial", 20, "bold"))
text.pack()

window.mainloop()
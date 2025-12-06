from customtkinter import *
window = CTk()
window.title("Чат з кнопками")
window.geometry("400*400")

text_field = CTkTextbox(window, width = 380, height = 280)
text_field.pack(pady = 10)

text_entry = CTkEntry(window, width = 380)
text_entry.pack(pady = 10)

button = CTkButton(window, text = "Введіть повідомлення", width = 380)
button.pack()

window.mainloop()
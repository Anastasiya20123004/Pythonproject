from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400 * 300")
        self.title("Соціальне опитування")
        self.configure(fg_color="purple")

        font = ("Arial", 30, "bold")
        self.text = CTkLabel(self, text = "Чи подобається тобі навчатися у школі Logika?", font = font, text_color = "white")
        self.text.pack()
        self.yes = CTkButton(self, text = "Так", compound = "right")
        self.yes.pack()
        self.no = CTkButton(self, text="Ні")
        self.no.configure(compound = "left")
        self.no.pack()

window = MainWindow()
window.mainloop()
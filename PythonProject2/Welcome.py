from customtkinter import *
from PIL import Image, ImageTk

class welcomeMenu(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400*400")
        self.title("Welcome Menu")
        self.resizable(True, False)


        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side = LEFT, fill = BOTH)
        img = Image.open("bg.png")
        CTk_img = CTkImage(light_image=img, size = (450, 400))
        self.img_label = CTkLabel(self.left_frame, text = "Welcome", image= CTk_img, font = ("Helvetica", 60, "bold"))
        self.img_label.pack()

        self.right_frame = CTkFrame(self, fg_color = "pink")
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand = True)

        font = ("Comic Relief", 20, "bold")
        CTkLabel(self.right_frame, text = "LogiTalk", font = font, text_color = "#ffffff").pack(pady = 60)
        self.name_entry = CTkEntry(self.right_frame, placeholder_text = '☻ ім`я', height=45, font=font, corner_radius = 25, fg_color = '#eae6ff', border_color='#eae6ff', text_color='#6753cc', placeholder_text_color='#6753cc')
        self.name_entry.pack(fill='x', padx=10)
        self.settings_button = CTkButton(self.right_frame, text = 'Налаштування', height = 45, corner_radius = 25, fg_color = '#eae6ff', font = font, text_color = '#6753cc', compound = 'left')
        self.settings_button.pack(fill='x', padx=5, pady = 11)

welcomeMenu().mainloop()
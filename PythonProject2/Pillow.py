from customtkinter import *
from PIL import Image

img = Image.open("3.png")
C_img = CTkImage(light_image=img, size=(50,50))

window = CTk()
label = CTkLabel(window, image=C_img, text ="")
label.pack()
window.mainloop()
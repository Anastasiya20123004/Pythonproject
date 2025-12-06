from customtkinter import *
from PIL import Image, ImageFilter

window = CTk()
window.geometry("600*450")
set_default_color_theme("blue")

image_CTk = CTkImage(light_image = Image.open("Cat.jpg"), size = (250, 300))
label_img = CTkLabel(window, image = image_CTk, text = " ")
label_img.pack(pady = 100)

set_frame = CTkFrame(window)
set_frame.pack(pady = 20, side = "bottom")

image = Image.open("Cat.jpg")
img_original = Image.open("Cat.jpg")
def do_wb():
    global image
    image = image.convert("L")
    image_CTk.configure(light_image=image)
    label_img.configure(image=image_CTk)

def do_blur():
    global image
    image = image.filter(ImageFilter.BLUR)
    image_CTk.configure(light_image = image)
    label_img.configure(image = image_CTk)

def do_original():
    global image
    image = img_original
    image_CTk.configure(light_image=image)
    label_img.configure(image=image_CTk)

def do_Save():
    global image
    image.save("Cat2.png")

btn_bw = CTkButton(set_frame, text = "BlackWhite")
btn_bw.grid(row = 0, column = 0,padx =  10)

btn_blur = CTkButton(set_frame, text = "BLUR")
btn_blur.grid(row = 0, column = 1, padx = 10)

btn_Original = CTkButton(set_frame, text = "Скинути")
btn_Original .grid(row = 0, column = 1, padx = 10)

btn_Save = CTkButton(set_frame, text="Зберегти", command=do_Save)
btn_Save.grid(row = 1, column = 1,pady =  10)

window.mainloop()
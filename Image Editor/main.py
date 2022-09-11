# imports
import tkinter as tk
import os
from turtle import width
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# path of py file declaration
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# window config
win = tk.Tk()
win.title("Mandela Catalogue Image Editor")
win.iconbitmap(os.path.join(__location__, "intruder.ico"))

# config of canvas
betterWin1 = tk.Canvas(win, width=400, height=300)
betterWin1.pack()

# some things in window
label1 = tk.Label(win, text="Type your name:")
label1.config(font=("helvetica", 10))
betterWin1.create_window(200, 120, window=label1)
entry1 = tk.Entry (win)
betterWin1.create_window(200, 140, window=entry1)

# function of image editing
def ImageEditing ():
    name = entry1.get()
    img = Image.open(os.path.join(__location__, "edit_img.png"))
    ManCatFont = ImageFont.truetype(os.path.join(__location__, "coolvetica rg.ttf"), 55)
    text1 = "bad decision, " + name
    draw = ImageDraw.Draw(img)
    center = draw.textlength(text1, font=ManCatFont)
    draw.text((((1439-center)/2)+20, 565), text1, font=ManCatFont)
    img = img.save("final.png")
    betterWin2 = tk.Toplevel(tk.Canvas(win, width=400, height=300))

# button config
buttonSubmit = tk.Button(text='Submit', command=ImageEditing)
betterWin1.create_window(200, 170, window=buttonSubmit)

# looping window
win.mainloop()

'''
    ManCatFont = Font(
        family="Coolvetica",
        size=49,
        weight="bold",
        underline=0,
        overstrike=0,
    )
# open image
img = Image.open('/home/ubuntu/image.png')

# draw image object
I1 = ImageDraw.Draw(img)

# add text to image
I1.text((28, 36), "hello world", fill=(255, 0, 0))

# save image
img.save("/home/ubuntu/image.png")
'''
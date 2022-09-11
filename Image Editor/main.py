# import libraries
# from tkinter import * 
import tkinter as tk
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
win = tk.Tk()
betterWin1 = tk.Canvas(win, width=400, height=300)
betterWin1.pack()
entry1 = tk.Entry (win)
betterWin1.create_window(200, 140, window=entry1)
entry2 = tk.Entry (win)
betterWin1.create_window(200, 160, window=entry2)
def ImageEditing ():
    pathImg = entry1.get()
    name = entry2.get()
    img = Image.open(os.path.join(__location__, "edit_img.png"))
    ManCatFont = ImageFont.truetype(os.path.join(__location__, "coolvetica rg.ttf"), 52)
    ImageDraw.Draw(img).text((730, 565), "bad decision, " + name, font=ManCatFont)
    img = img.save("final.png")
buttonSubmit = tk.Button(text='Submit', command=ImageEditing)
betterWin1.create_window(200, 180, window=buttonSubmit)
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
# import libraries
# from tkinter import * 
import tkinter as tk
from PIL import Image
from PIL import ImageDraw

win = tk.Tk()
betterWin1 = tk.Canvas(win, width=400, height=300)
betterWin1.pack()
entry1 = tk.Entry (win)
betterWin1.create_window(200, 140, window=entry1)
def getPath ():
    path = entry1.get()
    img = Image.open('')
win.mainloop()

'''

# open image
img = Image.open('/home/ubuntu/image.png')

# draw image object
I1 = ImageDraw.Draw(img)

# add text to image
I1.text((28, 36), "hello world", fill=(255, 0, 0))

# save image
img.save("/home/ubuntu/image.png")
'''
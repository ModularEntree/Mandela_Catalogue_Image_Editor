# imports
from pickle import TRUE
import tkinter as tk
import os
import sys
import pygame
import time
import threading
from turtle import delay, width
from tkinter.font import Font
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageTk

# path of py file declaration
# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(sys.executable)))
elif __file__:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# window config
win = tk.Tk()
win.title("Mandela Catalogue Image Editor")
win.iconbitmap(os.path.join(__location__, "./assets/Intruder.ico"))

# font and ending of a thread
AnaHor = Font(
    family="VCR OSD Mono",
    size=40,
    weight="bold",
    overstrike=0,
    underline=0
)
end = 0

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
    if name == "":
        name = "my child"
    img = Image.open(os.path.join(__location__, "./assets/edit_img.png"))
    ManCatFont = ImageFont.truetype(os.path.join(__location__, "./assets/coolvetica rg.ttf"), 55)
    text1 = "bad decision, " + name + "!"
    draw = ImageDraw.Draw(img)
    center = draw.textlength(text1, font=ManCatFont)
    draw.text((((1439-center)/2)+20, 565), text1, font=ManCatFont)
    img = img.save("final.png")

# threading of the Intruder in the background 
def background():
    i = 1
    while i<100:
        pygame.mixer.init()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join(__location__, "./assets/TheIntruderAlert.wav")))
        time.sleep(5)
        i+=1
        if end==1:
            break

# scary function or something idk i just need to practice this shit
def IntruderAlert ():
    # seting up the toplevel
    win2 = tk.Toplevel(win)
    win2.title("Mandela Catalogue Image Editor")
    win2.iconbitmap(os.path.join(__location__, "./assets/Intruder.ico"))
    win2.geometry("902x688")

    # background image settings
    global imgbg
    imgBg = Image.open(os.path.join(__location__, "./assets/Intruder.png")).resize((902, 688))
    imgbg = ImageTk.PhotoImage(imgBg)
    bg_label = tk.Label(win2, image=imgbg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    win2.update()

    # label settings
    label2 = tk.Label(win2, text="I am inside your home", font=AnaHor)
    label2.pack(pady=20)

    # settings of music in the background
    pygame.mixer.init()
    threading.Thread(name='background', target=background).daemon = True
    threading.Thread(name='background', target=background).start()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join(__location__, "./assets/Intruder.wav")))
    win2.mainloop()

# button config
buttonSubmit = tk.Button(text='Submit', command=lambda: [ImageEditing(), IntruderAlert()])
betterWin1.create_window(200, 170, window=buttonSubmit)

# looping window and ending program
win.mainloop()
end=1
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

o1 = Image.open('images/O.gif')
o2 = o1.resize((100, 100), Image.ANTIALIAS)
o3 = ImageTk.PhotoImage(o2)
Label(root, image=o3).pack()

x1 = Image.open('images/X.gif')
x2 = x1.resize((100, 100), Image.ANTIALIAS)
x3 = ImageTk.PhotoImage(x2)
Label(root, image=x3).pack()

mainloop()

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

o1 = Image.open('images/O.gif')
o2 = o1.resize((100, 100), Image.ANTIALIAS)
o3 = ImageTk.PhotoImage(o2)
Label(root, image=o3).pack()

empty1 = Image.open('images/Empty.gif')
empty2 = empty1.resize((100, 100), Image.ANTIALIAS)
empty3 = ImageTk.PhotoImage(empty2)
Label(root, image=empty3).pack()

x1 = Image.open('images/X.gif')
x2 = x1.resize((100, 100), Image.ANTIALIAS)
x3 = ImageTk.PhotoImage(x2)
Label(root, image=x3).pack()

mainloop()

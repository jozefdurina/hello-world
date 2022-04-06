from logging import root
from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')

frm = ttk.Frame(ws, padding=10)


text_box = Text(frm, height=1, width=5)

text_box1 = Text(frm, height=1, width=5)
text_box1.grid(column=0, row=1)

text_box2 = Text(frm, height=1, width=5)
text_box2.grid(column=0, row=2)

text_box3 = Text(frm, height=1, width=5)
text_box3.grid(column=0, row=3)

text_box4 = Text(frm, height=1, width=5)
text_box4.grid(column=0, row=4)

text_box5 = Text(frm, height=1, width=5)
text_box5.grid(column=0, row=5)

text_box6 = Text(frm, height=1, width=5)
text_box6.grid(column=1, row=1)

text_box7 = Text(frm, height=1, width=5)
text_box7.grid(column=1, row=2)

text_box8 = Text(frm, height=1, width=5)
text_box8.grid(column=1, row=3)

text_box9 = Text(frm, height=1, width=5)
text_box9.grid(column=1, row=4)

text_box9 = Text(frm, height=1, width=5)
text_box9.grid(column=1, row=5)


frm.mainloop()
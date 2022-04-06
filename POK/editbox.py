from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#A67449')

message ='''
Dear Reader,

    Don't let this situation
    blind your future. We at
    PythonGuides write tutorials
    with real life examples to 
    make you understand the concept
    in best possible way.

Thanks & Regards,
Team PythonGuides '''


mesage2= "ahoj"
text_box = Text(
    ws,
    height=1,
    width=5
)
text_box.pack(expand=True)
text_box.grid(column=0, row=1)

text_box2 = Text(
    ws,
    height=13,
    width=40
)
text_box2.grid(column=0, row=2)

ws.mainloop()
from tkinter import *

def extract_data():
    print(text_box.get('1.0', 'end'))


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')


message ='''
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
Ten
eleven
twelve 
thirteen
fourteen
fifteen 
sixteen
seventeen
eighteen
nineteen
twenty

'''

frame = Frame(ws)

text_box = Text(
    frame,
    height=13,
    width=20,
    wrap='word'
)
text_box.insert('end', message)
text_box.pack(side=LEFT,expand=True)


sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

text_box.config(yscrollcommand=sb.set)
sb.config(command=text_box.yview)

frame.pack(expand=True)

ws.mainloop()
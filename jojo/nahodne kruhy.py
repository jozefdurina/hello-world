import tkinter as tk
import threading
import random

timer:threading.Timer
timerInterval = 0.01
canvasWidth = 300
canvasHeight = 300
kruhy=[]

def getRandomColorCode():
    return "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])

def circle(cnv: tk.Canvas, x: int, y:int , r:int, fillColor:str):
    return cnv.create_oval(x-r, y-r, x+r, y+r, fill=fillColor)

def deleteRandomCircle(cnv: tk.Canvas):
    if len(kruhy)>4:
        idx=random.randint(0, len(kruhy)-1)
        cnv.delete(kruhy.pop(idx))


def paintRandomCircle(cnv: tk.Canvas):
    radius = random.randint(5,50)
    x=random.randint(-radius+1, canvasWidth+radius-1)
    y=random.randint(-radius+1, canvasHeight+radius-1)
    fillColor=getRandomColorCode()
    kruhy.append(circle(cnv, x, y, radius, fillColor))

def timerCallBack(cnv: tk.Canvas):
    paintRandomCircle(cnv)
    deleteRandomCircle(cnv)
    global timer
    timer = threading.Timer(timerInterval, lambda: timerCallBack(cnv))
    timer.start()

def start():
    global timer
    timer = threading.Timer(timerInterval, lambda: timerCallBack(cnv))
    timer.start()
    pauseStartBtn.configure(text="Pause", command=pause)

def pause():
    global timer
    timer.cancel()
    pauseStartBtn.configure(text="Štart", command=start)

random.seed()

root = tk.Tk()

cnv = tk.Canvas (root, width=canvasWidth, height=canvasHeight, bg="white")
cnv.grid(row=0, column=0, columnspan=2)

paintBtn = tk.Button(root, text="Pridaj", command=lambda: paintRandomCircle(cnv))
paintBtn.grid(row=1, column=0)

pauseStartBtn = tk.Button(root, text="Pause", command=pause)
pauseStartBtn.grid(row=1, column=1)

timerCallBack(cnv)

root.mainloop()

timer.cancel()



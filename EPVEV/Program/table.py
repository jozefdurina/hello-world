from string import whitespace
import tkinter  as tk 
from tkinter import * 


my_w = tk.Tk()
my_w.geometry("400x250") 


e=Label(my_w,width=10,text='id',borderwidth=2, relief='ridge',anchor='w', bg= "green")
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Class',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='mark',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text=main.Z012,borderwidth=2, relief='ridge',anchor='w',bg='yellow')    #???
e.grid(row=0,column=4)

i=1


my_w.mainloop()
from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
#from tkinter import messagebox

#definicie vypoctovych map

portaly= {
    "PORTÁL, kotevný"               :   [[-12,18.799],[0,18.799],[12,18.799],[-6,31.789],[6,31.789]],
    "PORTÁL, kotevný rozkročený"    :   [[1,2],[3,4],[5,6],[7,8],[9,10]]
}


root = Tk()
root.geometry("600x500")
root.title("Výpočet parametrov vedení")
#root2 = Tk()                             #Druhý rámík
frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(root2, padding=10)

frm.grid(row=0)
#frm2.grid(row=1)


ttk.Label(frm, text="Portál").grid(column=0, row=0)
ttk.Label(frm, text="Fázový vodič").grid(column=0, row=1)
ttk.Label(frm, text="Vodič zemného lana").grid(column=0, row=2)
ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
ttk.Label(frm, text="Minimálna výška vodiča").grid(column=0, row=4)
ttk.Label(frm, text="Kronova redukcia").grid(column=0, row=5)
ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=6)


#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


vypocitaj = ttk.Button(text="Vypočítaj",).grid()
vypocitaj2 = ttk.Button(text="Vypočítaj 2").grid()


labelTop = tk.Label(frm, text = "Počet vodičov vo zväzku")
labelTop.grid(column=0, row=7)


PortálCombo = ttk.Combobox(frm, state="readonly", values=list(portaly.keys()))
              
PortálCombo.grid(column=2, row=0)
#ortál.current(0)

#print(Portál.current(), Portál.get())

def debug_pressed():
    messagebox.showinfo("debug", PortálCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()

def checkcmbo():

     if PortálCombo.get() == "Kotevný":
         messagebox.showinfo("What user choose", "you choose prova")

fazovyVodicCombo = ttk.Combobox(frm, values=["185  AlFe 3",
"185  AlFe 6",
"185  AlFe 3",
"240  AlFe 6",
"350  AlFe 4",
"350  AlFe 6",
"450  AlFe 6",
"450  AlFe 8",
"500  AlFe 8",
"670  AlFe 8",])

fazovyVodicCombo.grid(column=2, row=1)


ttk.Combobox(frm, values=["185  AlFe 3",
"185  AlFe 6",
"185  AlFe 3",
"240  AlFe 6",
"350  AlFe 4",
"350  AlFe 6",
"450  AlFe 6",
"450  AlFe 8",
"500  AlFe 8",
"670  AlFe 8",]).grid(column=2, row=2)

ttk.Combobox(frm, values=["1",
"2",
"3",
"4"]).grid(column=2, row=3)
ttk.Combobox(frm, values=["aaa"]).grid(column=2, row=4)
ttk.Combobox(frm, values=["áno",
"nie"]).grid(column=2, row=5)
ttk.Combobox(frm, values=["Metóda komlexnej hlbky",
"Metóda Alvardo",
"Metóda 3",]).grid(column=2, row=6)
ttk.Combobox(frm, values=["1",
"2",
"3",
"4"]).grid(column=2, row=7)


root.mainloop()


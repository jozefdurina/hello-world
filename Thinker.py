from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox

#definicie vypoctovych map

stožiar = {
    "Kotevný"               :   [[-12,18.799],[0,18.799],[12,18.799],[-6,31.789],[6,31.789]],
    "Kotevný rozkročený"    :   [[1,2],[3,4],[5,6],[7,8],[9,10]]

}

vodič = {
    "185  AlFe 3"           :[],
    "185  AlFe 6"           :[],
    "185  AlFe 3"           :[],
    "240  AlFe 6"           :[],
    "350  AlFe 4"           :[],
    "350  AlFe 6"           :[],
    "450  AlFe 6"           :[],
    "450  AlFe 8"           :[],
    "500  AlFe 8"           :[],
    "670  AlFe 8"           :[],
}

# definícia okna

root = Tk()
root.geometry()
root.title("Výpočet parametrov vedení")
#root2 = Tk()                             #Druhý rámík
frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(root2, padding=10)

frm.grid(row=0)
#frm2.grid(row=1)


ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)
ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=1)
ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=2)
ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=4)
ttk.Label(frm, text="Kronova redukcia").grid(column=0, row=5)
ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=6)
labelTop = tk.Label(frm, text = "Počet vodičov vo zväzku")
labelTop.grid(column=0, row=7)





stožiarcombo = ttk.Combobox(frm, state="readonly", values=list(stožiar.keys()))        
stožiarcombo.grid(column=2, row=0)


fvodičcombo = ttk.Combobox(frm, state="readonly", values=list(vodič.keys()))
fvodičcombo.grid(column=2, row=1)


zlvodičcombo = ttk.Combobox(frm, state="readonly", values=list(vodič.keys()))
zlvodičcombo.grid(column=2, row=2)

pocetsystemcombo = ttk.Combobox(frm, state="readonly", values=["1","2","3","4"])
pocetsystemcombo.grid(column=2, row=3)


minvyska = ttk.Combobox(frm)
minvyska.grid(column=2, row=4)

cronoredukcia = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
cronoredukcia.grid(column=2, row=5)

metoda = ttk.Combobox(frm, values=["Metóda komlexnej hlbky","Metóda Alvardo","Metóda 3",])
metoda.grid(column=2, row=6)

zvazok = ttk.Combobox(frm, values=["1","2","3","4"])
zvazok.grid(column=2, row=7)

vypocitaj = ttk.Button(text="Vypočítaj",).grid()

def debug_pressed():
    messagebox.showinfo("debug", stožiarcombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()


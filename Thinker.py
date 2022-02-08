from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox



class Vodic: 
    def __init__(self, D, RAC20, dFE, prierez, pomer, E, rdc20, t_d):
        self.D = D
        self.RAC20 = RAC20
        self.dFE = dFE
        self.prierez = prierez
        self.pomer = pomer
        self.E = E
        self.rdc20 = rdc20
        self.t_d = t_d

class XY: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Stoziar: 
    def __init__(self, l1, l2, l3, zl1, zl2):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.zl1 = zl1
        self.zl2 = zl2

def konkretna_pocitacia_metoda():
    pass

def vypocitaj_pressed():
    #opracovavania
    ##bla bla
    konkretna_pocitacia_metoda()
    ##bla bla


#definicie vypoctovych map

stoziare = {
    "Kotevný"               : Stoziar(XY(-12, 18.799), XY(0, 18.799), XY(12, 18.799), XY(-6, 31.789), XY(6, 31.789)),
    "Kotevný rozkročený"    : Stoziar(XY(-12, 18.799), XY(0, 18.799), XY(12, 18.799), XY(-6, 31.789), XY(6, 31.789)),

}

vodice = {
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "185  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "240  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "350  AlFe 4"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "350  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "450  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "450  AlFe 8"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "500  AlFe 8"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "670  AlFe 8"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
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





stožiarcombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()))        
stožiarcombo.grid(column=2, row=0)


fvodičcombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
fvodičcombo.grid(column=2, row=1)


zlvodičcombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
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

vypocitaj = ttk.Button(text="Vypočítaj", command=vypocitaj_pressed).grid()

def debug_pressed():
    messagebox.showinfo("debug", stožiarcombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()


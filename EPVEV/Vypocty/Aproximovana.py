from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox
import math
import cmath


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

    @staticmethod
    def vzdialenost(b1, b2): #b1 a b2 su dva body typu XY
        return math.sqrt((b1.x-b2.x)**2 + (b1.y-b2.y)**2)

   


class Stoziar: 
    def __init__(self, a:XY, b:XY, c:XY, z1:XY, z2:XY):
        self.a = a
        self.b = b
        self.c = c
        self.z1 = z1
        self.z2 = z2

        

        self.m_vzd = [[0, XY.vzdialenost(a, b), XY.vzdialenost(a, c), XY.vzdialenost(a, z1), XY.vzdialenost(a, z2)],
            [XY.vzdialenost(b, a), 0, XY.vzdialenost(b, c), XY.vzdialenost(b, z1), XY.vzdialenost(b, z2)],
            [XY.vzdialenost(c, a), XY.vzdialenost(c, b), 0, XY.vzdialenost(c, z1), XY.vzdialenost(c, z2)],
            [XY.vzdialenost(z1,a), XY.vzdialenost(z1,b), XY.vzdialenost(z1,c),0, XY.vzdialenost(z1, z2)], 
            [XY.vzdialenost(z2,a), XY.vzdialenost(z2,b), XY.vzdialenost(z2,c), XY.vzdialenost(z2,z1),0]]





#definicie vypoctovych map

stoziare = {
    "Kotevný"               : Stoziar(XY(-12, 18.799), XY(0, 18.799), XY(12, 18.799), XY(-6, 31.789), XY(6, 31.789)),
    "Kotevný rozkročený"    : Stoziar(XY(-13, 18.736), XY(0, 18.736), XY(12, 18.736), XY(-7, 31.726), XY(7, 31.726)),

}

vodice = {
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "185  AlFe 6"           :Vodic(19.08, 0.1570, 7.08, 214.4, 6, 0.8, 0.1562, 0.314465 ),
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

frm = ttk.Frame(root, padding=10)


frm.grid(row=0)



ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)
ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=1)
ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=2)





stoziarCombo = ttk.Combobox(frm, values=list(stoziare))        
stoziarCombo.grid(column=2, row=0)


fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
fvodicCombo.grid(column=2, row=1)


zlvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
zlvodicCombo.grid(column=2, row=2)


def aproximovana_metoda():
    fvodic = vodice[fvodicCombo.get()]
    stoziar = stoziare[stoziarCombo.get()]
    
    E = fvodic.E
    Rg = 49.3   #[mΩ.m−1]
    mi0 = 1.25663706212E-6 #[H/m]
    dg = 796.039 #[m]
    D = 10.5 #mm
    r = D/2
    f = 50 #Hz
    ω = 2*math.pi*f
    
    
    Rik = Rg    #[Ω/km]
    Rii = fvodic.RAC20 + Rg
    #Zik = Rik + j*ω*Lik


    L = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    R = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    Z = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

    induk = L

    for i in range(5):
        for k in range(5):
            if i==k:
                L[i][k] = (mi0/2*math.pi) * cmath.log10(dg/E*r)   #zistit ci treba r
            else: 
                L[i][k] = (mi0/2*math.pi) * cmath.log10(dg/stoziar.m_vzd[i][k])




vypocitaj = ttk.Button(text="Vypočítaj", command=aproximovana_metoda).grid()

def debug_pressed():
    messagebox.showinfo("debug", aproximovana_metoda(induk))

debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()

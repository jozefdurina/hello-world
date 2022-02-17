from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox
import math

import metoda_komplexnej_hlbky as mkh


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

    def vzdialenost(self, bod):
        return math.sqrt((self.x-bod.x)**2 + (self.y-bod.y)**2)


class Stoziar: 
    def __init__(self, a:XY, b:XY, c:XY, z1:XY, z2:XY):
        self.a = a
        self.b = b
        self.c = c
        self.z1 = z1
        self.z2 = z2

        """self.ab = XY.vzdialenost(a, b)
        self.ac = XY.vzdialenost(a, c)
        self.bc = b.vzdialenost(c)
        self.az1 = XY.vzdialenost(a, z1)
        self.az2 = XY.vzdialenost(a, z2)
        self.bz1 = XY.vzdialenost(b, z1)
        self.bz2 = XY.vzdialenost(b, z2)
        self.cz1 = XY.vzdialenost(c, z1)
        self.cz2 = XY.vzdialenost(c, z2) """

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
#root2 = Tk()                             #Druhý rámík
frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(root2, padding=10)

frm.grid(row=0)
#frm2.grid(row=1)


ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)
ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=1)
ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=2)
# ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
# ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=4)
# ttk.Label(frm, text="Kronova redukcia").grid(column=0, row=5)
# ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=6)
# labelTop = tk.Label(frm, text = "Počet vodičov vo zväzku")
# labelTop.grid(column=0, row=7)





stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()))        
stoziarCombo.grid(column=2, row=0)


fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
fvodicCombo.grid(column=2, row=1)


zlvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
zlvodicCombo.grid(column=2, row=2)

# pocetSystemCombo = ttk.Combobox(frm, state="readonly", values=["1","2","3","4"])
# pocetSystemCombo.grid(column=2, row=3)


# minvyska = ttk.Combobox(frm)
# minvyska.grid(column=2, row=4)

# cronoredukcia = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
# cronoredukcia.grid(column=2, row=5)

# metodaCombo = ttk.Combobox(frm, values=["Metóda komlexnej hlbky","Metóda Alvardo","Metóda 3", "Aproximovana",])
# metodaCombo.grid(column=2, row=6)

# zvazokCombo = ttk.Combobox(frm, values=["1","2","3","4"])
# zvazokCombo.grid(column=2, row=7)

# def matica3():

#     for i in range(3):
#         for k in range(3):
#             if i==k

# def matica5():            

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
    Lik = (mi0/2*math.pi) * math.ln(dg/stoziar.m_vzd[i][k])
    Lii = (mi0/2*math.pi)*math.ln(dg/E*r)
    Rik = Rg    #[Ω/km]
    Rii = fvodic.RAC20 + Rg
    Zik = Rik + j**Lik


    L = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    R = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    Z = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

    for i in range(5):
        for k in range(5):
            if i==k:
                L[i][k] = (mi0/2*math.pi) * math.ln(dg/E*r)   #zistit ci treba r
            else: 
                L[i][k] = (mi0/2*math.pi) * math.ln(dg/stoziar.m_vzd[i][k])

def vypocitaj_pressed():

    #if metodaCombo.get() == "Aproximovana":
    #    aproximovana_metoda()
    

    stoziar = stoziare["Kotevný"]
    fvodic = vodice["185  AlFe 3"]
    result = mkh.metoda_bezZL(stoziar, fvodic)
    #result vypises do grafickeho okna



vypocitaj = ttk.Button(text="Vypočítaj", command=vypocitaj_pressed).grid()

def debug_pressed():
    messagebox.showinfo("debug", stoziarCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()


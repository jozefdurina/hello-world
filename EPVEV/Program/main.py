from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox
import math

import vypoctove_metody


class Vodic: 
    def __init__(self, D, RAC20, dFE, prierez, pomer, E, rdc20, t_d):
        self.D = D              #v mm
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

    def vzdialenost(self, bod):
        return math.sqrt((self.x-bod.x)**2 + (self.y-bod.y)**2)


class Stoziar: 
    def __init__(self, a:XY, b:XY, c:XY, z1:XY, z2:XY):
        self.a = a
        self.b = b
        self.c = c
        self.z1 = z1
        self.z2 = z2

        self.m_vzd = [
            [ 0               , a .vzdialenost(b), a .vzdialenost(c), a .vzdialenost(z1), a .vzdialenost(z2)],
            [ b.vzdialenost(a), 0                , b .vzdialenost(c), b .vzdialenost(z1), b .vzdialenost(z2)],
            [ c.vzdialenost(a), c .vzdialenost(b), 0                , c .vzdialenost(z1), c .vzdialenost(z2)],
            [z1.vzdialenost(a), z1.vzdialenost(b), z1.vzdialenost(c), 0                 , z1.vzdialenost(z2)],
            [z2.vzdialenost(a), z2.vzdialenost(b), z2.vzdialenost(c), z2.vzdialenost(z1), 0                 ],
        ]





#definicie vypoctovych map

stoziare = {
    "Kotevný"                                : Stoziar(XY(-12.00, 18.799), XY(0, 18.799), XY(12.00, 18.799), XY(-6.0, 31.789), XY(6.0, 31.789)),
    "Kotevný rozkročený"                     : Stoziar(XY(-13.00, 18.736), XY(0, 18.736), XY(13.00, 18.736), XY(-7.0, 31.726), XY(7.0, 31.726)),
    "Kotevný typ 1"                          : Stoziar(XY(-12.00, 18.000), XY(0, 18.000), XY(12.00, 18.000), XY(-6.0, 28.600), XY(6.0, 28.600)),
    "Kotevný typ 3 širší pôvodný "           : Stoziar(XY(-12.63, 18.000), XY(0, 18.000), XY(12.63, 18.000), XY(-6.0, 30.890), XY(6.0, 30.890)),
    "Nosný úzky"                             : Stoziar(XY(-11.00, 18.000), XY(0, 18.000), XY(11.00, 18.000), XY(-5.5, 31.025), XY(5.5, 31.025)),
    "Nosný rozkročený"                       : Stoziar(XY(-12.00, 18.200), XY(0, 18.200), XY(12.00, 18.200), XY(-6.0, 31.025), XY(6.0, 31.025)),
}

vodice = {
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.60, 3.00, 0.8260, 0.1593, 0.242521),
    "185  AlFe 6"           :Vodic(19.08, 0.1570, 7.08, 214.40, 6.00, 0.8000, 0.1250, 0.314465),
    "240  AlFe 6"           :Vodic(21.35, 0.1263, 7.95, 267.77, 6.00, 0.8000, 0.1250, 0.313817),
    "350  AlFe 4"           :Vodic(26.80, 0.0910, 11.8, 414.40, 3.99, 0.8212, 0.0888, 0.279851),
    "350  AlFe 4 test"      :Vodic(26.80, 0.0888, 11.8, 414.40, 3.99, 0.8212, 0.0888, 0.279851),
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


ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=0)
ttk.Label(frm, text="Typ stožiara").grid(column=0, row=1)
ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=2)
ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=3)
# ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
# ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=4)
# ttk.Label(frm, text="Kronova redukcia").grid(column=0, row=5)

# labelTop = tk.Label(frm, text = "Počet vodičov vo zväzku")
# labelTop.grid(column=0, row=7)



metodaCombo = ttk.Combobox(frm, values=["Metóda komlexnej hĺbky", "Aproximovaná",])
metodaCombo.grid(column=2, row=0)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()))        
stoziarCombo.grid(column=2, row=1)


fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
fvodicCombo.grid(column=2, row=2)


zlvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
zlvodicCombo.grid(column=2, row=3)

# pocetSystemCombo = ttk.Combobox(frm, state="readonly", values=["1","2","3","4"])
# pocetSystemCombo.grid(column=2, row=3)


# minvyska = ttk.Combobox(frm)
# minvyska.grid(column=2, row=4)

# cronoredukcia = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
# cronoredukcia.grid(column=2, row=5)



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
    stoziar = stoziare[stoziarCombo.get()]
    fvodic = vodice[fvodicCombo.get()]

    if metodaCombo.get() == "Aproximovaná":    
        result = vypoctove_metody.aproximovana_metoda(fvodic, stoziar)        

    if metodaCombo.get() == "Metóda komlexnej hĺbky":    
        result = vypoctove_metody.metoda_komplexnej_hlbky(fvodic, stoziar)            

    #stoziar = stoziare["Kotevný"]
    #fvodic = vodice["350  AlFe 4 test"]
    
    #result vypises do grafickeho okna



vypocitaj = ttk.Button(text="Vypočítaj", command=vypocitaj_pressed).grid()

def debug_pressed():
    messagebox.showinfo("debug", stoziarCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()


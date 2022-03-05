from re import L
from runpy import _ModifiedArgv0
from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox
import math



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

        self.az = XY(a.x, -a.y)     #az je zrkadlovy obraz fazoveho vodica a
        self.bz = XY(b.x, -b.y)
        self.cz = XY(c.x, -c.y)
        self.z1z = XY(z1.x, -z1.y)
        self.z2z = XY(z2.x, -z2.y)

        

        self.m_vzd = [[0, XY.vzdialenost(a, b), XY.vzdialenost(a, c), XY.vzdialenost(a, z1), XY.vzdialenost(a, z2)],
            [XY.vzdialenost(b, a), 0, XY.vzdialenost(b, c), XY.vzdialenost(b, z1), XY.vzdialenost(b, z2)],
            [XY.vzdialenost(c, a), XY.vzdialenost(c, b), 0, XY.vzdialenost(c, z1), XY.vzdialenost(c, z2)],
            [XY.vzdialenost(z1,a), XY.vzdialenost(z1,b), XY.vzdialenost(z1,c),0, XY.vzdialenost(z1, z2)], 
            [XY.vzdialenost(z2,a), XY.vzdialenost(z2,b), XY.vzdialenost(z2,c), XY.vzdialenost(z2,z1),0]]

        self.m_vzd_obrazov = [[0, XY.vzdialenost(a, b), XY.vzdialenost(a, c), XY.vzdialenost(a, z1), XY.vzdialenost(a, z2)],
            [XY.vzdialenost(b, a), 0, XY.vzdialenost(b, c), XY.vzdialenost(b, z1), XY.vzdialenost(b, z2)],
            [XY.vzdialenost(c, a), XY.vzdialenost(c, b), 0, XY.vzdialenost(c, z1), XY.vzdialenost(c, z2)],
            [XY.vzdialenost(z1,a), XY.vzdialenost(z1,b), XY.vzdialenost(z1,c),0, XY.vzdialenost(z1, z2)], 
            [XY.vzdialenost(z2,a), XY.vzdialenost(z2,b), XY.vzdialenost(z2,c), XY.vzdialenost(z2,z1),0]]



#definicie vypoctovych map

stoziare = {
    "Kotevný"               : Stoziar(XY(-12, 18.799), XY(0, 18.799), XY(12, 18.799), XY(-6, 31.789), XY(6, 31.789)),
    "Kotevný rozkročený"    : Stoziar(XY(-12, 12.799), XY(0, 12.799), XY(12, 12.799), XY(-6, 51.789), XY(6, 51.789)),

}

vodice = {
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "185  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "240  AlFe 6"           :Vodic(20.39, 0.1609, 10.5, 235.6, 3, 0.8260, 0.1593, 0.242521 ),
    "350  AlFe 4"           :Vodic(26.8, 0.0888, 11.8, 414.4, 3.99, 0.8212, 0.0888, 0.279851 ),
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


stoziarCombo = ttk.Combobox(frm, state=list(stoziare.keys()), values=list(stoziare.keys()))        
stoziarCombo.grid(column=2, row=0)


fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
fvodicCombo.grid(column=2, row=1)


zlvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vodice.keys()))
zlvodicCombo.grid(column=2, row=2)

def vypisMatice(M): # M je matica - definovana ako list listov
    for i in range(len(M)):
        print(M[i])    
    # print("\n")    

def aproximovana_metoda(fvodic, stoziar):
    D = fvodic.D/1000
    r = D/2
    E = fvodic.E
    Rg = 0.049300   #[Ω.km−1]
    mi0 = 4*math.pi*10**-4 #[H/km]
    print(mi0)
    dg = 982.878 #[m]
   # Zik = Rik + jωLik
    Rik = Rg    #[Ω/km]
    Rii = fvodic.rdc20 + 3*Rg

    L = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    R = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    Z = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

    for i in range(5):
        for k in range(5):
            if i==k:
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/(E*r), math.e)   #zistit ci treba r
                R[i][k] = Rii
                Z[i][k] = Rii+1j*L[i][k]*100*math.pi
            else: 
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/stoziar.m_vzd[i][k], math.e)
                R[i][k] = Rik
                Z[i][k] = Rik+1j*L[i][k]*100*math.pi


    q = print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica R\n")
    vypisMatice(R)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica L\n")
    vypisMatice(L)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica Z\n")
    vypisMatice(Z)

    #ttk.Label(frm, text= q).grid(column=0, row=5)
    #ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=6)
    #ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=7)

def komplexnej_hlbky():
    pass

def sunde():
    pass

def alvardo():
    pass

def carson():
    pass

def aproximovana_metoda_click():
    #fvodic = vodice[fvodicCombo.get()]
    #stoziar = stoziare[stoziarCombo.get()]
    #aproximovana_metoda(fvodic, stoziar)
    aproximovana_metoda(vodice["185  AlFe 3"] , stoziare["Kotevný"])


vypocitaj = ttk.Button(text="Vypočítaj", command=aproximovana_metoda_click).grid()

def debug_pressed():
    messagebox.showinfo("debug", stoziarCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()

#ttk.Label(frm, text=vypisMatice(aproximovana_metoda)).grid(column=0, row=5)
#ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=6)
#ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=7)
root.mainloop()


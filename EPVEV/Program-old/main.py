from email import message
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
import tkinter as tk
from turtle import right
from unicodedata import name
from tkinter import messagebox
import math
import copy

import matplotlib.pyplot as plt

import Kronova_redukcia 
import Zlozkova_sustava
import vypoctove_mapy
import Aproximovana_metoda


################################################################################################################
# definícia okna 

root = Tk()
root.title("Výpočet parametrov vedení")


################################################################################################################
# definicia ramika

frm = ttk.Frame(root, padding=10)
frm.grid()
frm.grid_rowconfigure(5, minsize=50)
frm.grid_rowconfigure(7, minsize=50)


################################################################################################################
# Stoziar

ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)


def stoziar_changed(index, value, op):
    L1x_fv.delete("1.0","end")
    L1x_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L1.x))
    L1y_fv.delete("1.0","end")
    L1y_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L1.y))
    L2x_fv.delete("1.0","end")
    L2x_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L2.x))
    L2y_fv.delete("1.0","end")
    L2y_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L2.y))
    L3x_fv.delete("1.0","end")
    L3x_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L3.x))
    L3y_fv.delete("1.0","end")
    L3y_fv.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].L3.y))
    ZL1x_zl.delete("1.0","end")
    ZL1x_zl.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].ZL1.x))
    ZL1y_zl.delete("1.0","end")
    ZL1y_zl.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].ZL1.y))
    ZL2x_zl.delete("1.0","end")
    ZL2x_zl.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].ZL2.x))
    ZL2y_zl.delete("1.0","end")
    ZL2y_zl.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].ZL2.y))

vStoziar = StringVar()
vStoziar.trace('w', stoziar_changed)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.stoziare.keys()), textvar=vStoziar, width=25)        
stoziarCombo.grid(column=1, row=0)

ttk.Label(frm, text="L1x", width=10, anchor = "e").grid(column=3, row=1)
ttk.Label(frm, text="L1y", width=10, anchor = "e").grid(column=3, row=2)
L1x_fv = Text(frm, height=1, width=7)
L1x_fv.grid(column=4, row=1)
L1y_fv = Text(frm, height=1, width=7)
L1y_fv.grid(column=4, row=2)

ttk.Label(frm, text="L2x", width=10, anchor = "e").grid(column=5, row=1)
ttk.Label(frm, text="L2y", width=10, anchor = "e").grid(column=5, row=2)
L2x_fv = Text(frm, height=1, width=7)
L2x_fv.grid(column=6, row=1)
L2y_fv = Text(frm, height=1, width=7)
L2y_fv.grid(column=6, row=2)

ttk.Label(frm, text="L3x", width=10, anchor = "e").grid(column=7, row=1)
ttk.Label(frm, text="L3y", width=10, anchor = "e").grid(column=7, row=2)
L3x_fv = Text(frm, height=1, width=7)
L3x_fv.grid(column=8, row=1)
L3y_fv = Text(frm, height=1, width=7)
L3y_fv.grid(column=8, row=2)



ttk.Label(frm, text="ZL1x",  width=10, anchor = "e").grid(column=9, row=1)
ttk.Label(frm, text="ZL1y",  width=10, anchor = "e").grid(column=9, row=2)
ZL1x_zl = Text(frm, height=1, width=7)
ZL1x_zl.grid(column=10, row=1)
ZL1y_zl = Text(frm, height=1, width=7)
ZL1y_zl.grid(column=10, row=2)

ttk.Label(frm, text="ZL2x",  width=10, anchor = "e").grid(column=11, row=1)
ttk.Label(frm, text="ZL2y",  width=10, anchor = "e").grid(column=11, row=2)
ZL2x_zl = Text(frm, height=1, width=7)
ZL2x_zl.grid(column=12, row=1)
ZL2y_zl = Text(frm, height=1, width=7)
ZL2y_zl.grid(column=12, row=2)


frm.grid_rowconfigure(1, minsize=20)
frm.grid_rowconfigure(2, minsize=50)


################################################################################################################
#Fazovy vodic

def fv_changed(index, value, op):
    D_fv.delete("1.0","end")
    D_fv.insert('end', str(vypoctove_mapy.vodice[fvodicCombo.get()].D))
    dFE_fv.delete("1.0","end")
    dFE_fv.insert('end', str(vypoctove_mapy.vodice[fvodicCombo.get()].dFE))
    prierez_fv.delete("1.0","end")
    prierez_fv.insert('end', str(vypoctove_mapy.vodice[fvodicCombo.get()].prierez))
    pomer_fv.delete("1.0","end")
    pomer_fv.insert('end', str(vypoctove_mapy.vodice[fvodicCombo.get()].pomer))
    td_fv.delete("1.0","end")
    td_fv.insert('end', str(vypoctove_mapy.vodice[fvodicCombo.get()].t_d))


vFv = StringVar()
vFv.trace('w', fv_changed)

ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=4)
frm.grid_rowconfigure(4, minsize=50)

fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()), textvar=vFv, width=25)
fvodicCombo.grid(column=1, row=4)

ttk.Label(frm, text="D", width=10, anchor = "e").grid(column=3, row=5)
D_fv = Text(frm, height=1, width=7)
D_fv.grid(column=4, row=5)

ttk.Label(frm, text="dFE",  width=10, anchor = "e").grid(column=5, row=5)
dFE_fv = Text(frm, height=1, width=7)
dFE_fv.grid(column=6, row=5)

ttk.Label(frm, text="prierez",  width=10, anchor = "e").grid(column=7, row=5)
prierez_fv = Text(frm, height=1, width=7)
prierez_fv.grid(column=8, row=5)

ttk.Label(frm, text="pomer",  width=10, anchor = "e").grid(column=9, row=5)
pomer_fv = Text(frm, height=1, width=7)
pomer_fv.grid(column=10, row=5)

ttk.Label(frm, text="td",  width=10, anchor = "e").grid(column=11, row=5)
td_fv = Text(frm, height=1, width=7)
td_fv.grid(column=12, row=5)


################################################################################################################
#Zemne lana

def zl_changed(index, value, op):
    D_zl.delete("1.0","end")
    D_zl.insert('end', str(vypoctove_mapy.vodice[zvodicCombo.get()].D))
    dFE_zl.delete("1.0","end")
    dFE_zl.insert('end', str(vypoctove_mapy.vodice[zvodicCombo.get()].dFE))
    prierez_zl.delete("1.0","end")
    prierez_zl.insert('end', str(vypoctove_mapy.vodice[zvodicCombo.get()].prierez))
    pomer_zl.delete("1.0","end")
    pomer_zl.insert('end', str(vypoctove_mapy.vodice[zvodicCombo.get()].pomer))
    td_zl.delete("1.0","end")
    td_zl.insert('end', str(vypoctove_mapy.vodice[zvodicCombo.get()].t_d))


vZl = StringVar()
vZl.trace('w', zl_changed)

ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=6)
frm.grid_rowconfigure(6, minsize=50)

zvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()), textvar=vZl, width=25)
zvodicCombo.grid(column=1, row=6)

ttk.Label(frm, text="D",  width=10, anchor = "e").grid(column=3, row=7)
D_zl = Text(frm, height=1, width=7)
D_zl.grid(column=4, row=7)

ttk.Label(frm, text="dFE",  width=10, anchor = "e").grid(column=5, row=7)
dFE_zl = Text(frm, height=1, width=7)
dFE_zl.grid(column=6, row=7)

ttk.Label(frm, text="prierez",  width=10, anchor = "e").grid(column=7, row=7)
prierez_zl = Text(frm, height=1, width=7)
prierez_zl.grid(column=8, row=7)

ttk.Label(frm, text="pomer",  width=10, anchor = "e").grid(column=9, row=7)
pomer_zl = Text(frm, height=1, width=7)
pomer_zl.grid(column=10, row=7)

ttk.Label(frm, text="td",  width=10, anchor = "e").grid(column=11, row=7)
td_zl = Text(frm, height=1, width=7)
td_zl.grid(column=12, row=7)


################################################################################################################
#Zvazok

ttk.Label(frm, text = "Počet vodičov vo zväzku").grid(column=0, row=13)
frm.grid_rowconfigure(13, minsize=50)

zvazokCombo = ttk.Combobox(frm, state="readonly", values=["1","2","3"], width=25)
zvazokCombo.grid(column=1, row=13)

ttk.Label(frm, text="krok zvazku", width=10, anchor = "e").grid(column=3, row=14)
krok_zvazok = Text(frm, height=1, width=7)
krok_zvazok.grid(column=4, row=14)
frm.grid_rowconfigure(14, minsize=50)

################################################################################################################
#Minimalna vyska

ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=15)
frm.grid_rowconfigure(15, minsize=100)

min_vyska = Text(frm, height=1, width=20)
min_vyska.grid(column=1, row=15)


################################################################################################################
#Automaticky vypocet


ttk.Label(frm, text = "Menený vstupný parameter").grid(column=0, row=17)
frm.grid_rowconfigure(17, minsize=50)

vstup_param = ttk.Combobox(frm, state="readonly", width=25, values=["L1x", "L1y", "L2x", "L2y", "L3x", "L3y", "ZL1x", "ZL1y", "ZL2x", "ZL2y", "D.fv", "dFE.fv", "prierez.fv", "pomer.fv", "td.fv", "D.zl", "dFE.zl", "prierez.zl", "pomer.zl", "td.zl"  ])
vstup_param.grid(column=1, row=17)

ttk.Label(frm, text="rozsah od",  width=10, anchor = "e").grid(column=3, row=18)
rozsah_od = Text(frm, height=1, width=7)
rozsah_od.grid(column=4, row=18)

ttk.Label(frm, text="rozsah do",  width=10, anchor = "e").grid(column=5, row=18)
rozsah_do = Text(frm, height=1, width=7)
rozsah_do.grid(column=6, row=18)

ttk.Label(frm, text="krok rozsahu",  width=10, anchor = "e").grid(column=7, row=18)
krok_rozsah= Text(frm, height=1, width=7)
krok_rozsah.grid(column=8, row=18)

frm.grid_rowconfigure(18, minsize=50)


################################################################################################################

def ziskaj_vstupy():
    L1 = vypoctove_mapy.XY(float(L1x_fv.get("1.0",END)), float(L1y_fv.get("1.0",END)))
    L2 = vypoctove_mapy.XY(float(L2x_fv.get("1.0",END)), float(L2y_fv.get("1.0",END)))
    L3 = vypoctove_mapy.XY(float(L3x_fv.get("1.0",END)), float(L3y_fv.get("1.0",END)))
    ZL1 = vypoctove_mapy.XY(float(ZL1x_zl.get("1.0",END)), float(ZL1y_zl.get("1.0",END)))
    ZL2 = vypoctove_mapy.XY(float(ZL2x_zl.get("1.0",END)), float(ZL2y_zl.get("1.0",END)))

    stoziar = vypoctove_mapy.Stoziar(L1, L2, L3, ZL1, ZL2)

    fvodic = copy.copy(vypoctove_mapy.vodice[fvodicCombo.get()])
    fvodic.setD         (float(D_fv.get("1.0",END)))
    fvodic.setdFE       (float(dFE_fv.get("1.0",END)))
    fvodic.setprierez   (float(prierez_fv.get("1.0",END)))
    fvodic.setpomer     (float(pomer_fv.get("1.0",END)))
    fvodic.sett_d       (float(td_fv.get("1.0",END)))


    zvodic = copy.copy(vypoctove_mapy.vodice[zvodicCombo.get()])
    zvodic.setD         (float(D_zl.get("1.0",END)))
    zvodic.setdFE       (float(dFE_zl.get("1.0",END)))
    zvodic.setprierez   (float(prierez_zl.get("1.0",END)))
    zvodic.setpomer     (float(pomer_zl.get("1.0",END)))
    zvodic.sett_d       (float(td_zl.get("1.0",END)))

    krokzv = int(krok_zvazok.get("1.0",END))
    zvazok = float(zvazokCombo.get())

    return stoziar, fvodic, zvodic, krokzv, zvazok

def vypocitaj_pressed():
    stoziar, fvodic, zvodic, krokzv, zvazok = ziskaj_vstupy()    

    stoziar.prepocitaj_m_vzd()

    Z = Aproximovana_metoda.aproximovana_metoda(fvodic, zvodic, stoziar, krokzv, zvazok)
    Zabc = Kronova_redukcia.kronovaRedukcia(Z)
    Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)

def analyzuj_pressed():
    stoziar, fvodic, zvodic, krokzv, zvazok = ziskaj_vstupy()    
    
    od = float(rozsah_od.get("1.0",END))
    do = float(rozsah_do.get("1.0",END))
    krokr = float(krok_rozsah.get("1.0",END))

    meneny = vstup_param.get()

    import numpy as np

    x = np.arange(od, do , krokr)
    y = []
 
    for i in x:
        if meneny=="L1x":
            stoziar.L1.setX(i)            
        elif meneny == "L1y":
            stoziar.L1.setY(i)
        elif meneny=="D.fv":
            fvodic.setD(i)

        stoziar.prepocitaj_m_vzd()

        Z = Aproximovana_metoda.aproximovana_metoda(fvodic, zvodic, stoziar, krokzv, zvazok)
        Zabc = Kronova_redukcia.kronovaRedukcia(Z)
        Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)

        y.append(np.imag(Z012[0][0]))
    
    plt.plot(x, y)
    plt.show()





    # vysledky = []
    # for i in range(pocet_krokov): # podla poctu krokov
    #     Z = Aproximovana_metoda.aproximovana_metoda(fvodic, zvodic, stoziar, krok, zvazok)
    #     Zabc = Kronova_redukcia.kronovaRedukcia(Z)
    #     Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)
    #     vysledky.append(Z012)

    # zakresli(vysledky, nezavisla, zavisla)
    # zapisDoExcelu(vysledky)
    #vysledky[0][0][0].realna_cast()



ttk.Button(text="Vypočítaj", command=vypocitaj_pressed).grid()

def debug_pressed():
    messagebox.showinfo("debug", stoziarCombo["values"])

ttk.Button(text="Analyzuj", command=analyzuj_pressed).grid()


def table_pressed():
    messagebox.showinfo("debug", stoziarCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()


def graf_pressed():
    messagebox.showinfo("Tabulka", stoziarCombo["values"])

debug = ttk.Button(text="Graf", command=debug_pressed).grid()




root.mainloop()

print("koniec")

from email import message
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name
from tkinter import messagebox
import math

import vypoctove_metody
import Kronova_redukcia 
import Zlozkova_sustava
import vypoctove_mapy


# definícia okna

root = Tk()
root.geometry()
root.title("Výpočet parametrov vedení")
#root2 = Tk()                            #Druhý rámík

frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(frm1, padding=10)

frm.grid()
#frm2.grid(column=0)

# Stoziar

a = ttk.Label(frm, text="Typ stožiara")
a.grid(column=0, row=0)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.stoziare.keys()))        
stoziarCombo.grid(column=1, row=0)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=3, row=1)
L1y = ttk.Label(frm, text="L1y")
L1y.grid(column=3, row=2)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=4, row=1)
L1y_read = Text(frm, height=1, width=5)
L1y_read.grid(column=4, row=2)

L2x = ttk.Label(frm, text="L2x")
L2x.grid(column=5, row=1)
L2y = ttk.Label(frm, text="L2y")
L2y.grid(column=5, row=2)
L2x_read = Text(frm, height=1, width=5)
L2x_read.grid(column=6, row=1)
L2y_read = Text(frm, height=1, width=5)
L2y_read.grid(column=6, row=2)

L3x = ttk.Label(frm, text="L3x")
L3x.grid(column=7, row=1)
L3y = ttk.Label(frm, text="L3y")
L3y.grid(column=7, row=2)
L3x_read = Text(frm, height=1, width=5)
L3x_read.grid(column=8, row=1)
L3y_read = Text(frm, height=1, width=5)
L3y_read.grid(column=8, row=2)

ZL1x = ttk.Label(frm, text="ZL1x")
ZL1x.grid(column=9, row=1)
ZL1y = ttk.Label(frm, text="ZL1y")
ZL1y.grid(column=9, row=2)
ZL1x_read = Text(frm, height=1, width=5)
ZL1x_read.grid(column=10, row=1)
ZL1y_read = Text(frm, height=1, width=5)
ZL1y_read.grid(column=10, row=2)

ZL2x = ttk.Label(frm, text="ZL2x")
ZL2x.grid(column=11, row=1)
ZL2y = ttk.Label(frm, text="ZL2y")
ZL2y.grid(column=11, row=2)
ZL2x_read = Text(frm, height=1, width=5)
ZL2x_read.grid(column=12, row=1)
ZL2y_read = Text(frm, height=1, width=5)
ZL2y_read.grid(column=12, row=2)


#Fazovy vodic

ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=4)

fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()))
fvodicCombo.grid(column=1, row=4)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=3, row=5)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=4, row=5)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=5, row=5)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=6, row=5)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=7, row=5)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=8, row=5)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=9, row=5)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=10, row=5)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=11, row=5)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=12, row=5)

#Zemne lana

ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=6)

zvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()))
zvodicCombo.grid(column=1, row=6)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=3, row=7)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=4, row=7)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=5, row=7)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=6, row=7)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=7, row=7)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=8, row=7)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=9, row=7)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=10, row=7)

L1x = ttk.Label(frm, text="L1x")
L1x.grid(column=11, row=7)
L1x_read = Text(frm, height=1, width=5)
L1x_read.grid(column=12, row=7)

#Zvazok

ttk.Label(frm, text = "Počet vodičov vo zväzku").grid(column=0, row=13)

zvazokCombo = ttk.Combobox(frm, values=["1","2","3"])
zvazokCombo.grid(column=1, row=13)

krok = ttk.Label(frm, text="krok")
krok.grid(column=3, row=14)
krok_read = Text(frm, height=1, width=5)
krok_read.grid(column=4, row=14)

#Minimalna vyska

ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=15)

min_vyska = Text(frm, height=1, width=17)
min_vyska.grid(column=1, row=15)



# ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=6)
# ttk.Label(frm, text= "Kronova redukcia").grid(column=0, row=7)
# ttk.Label(frm, text= "Zlozkova sustava").grid(column=0, row=8)
# ttk.Label(frm, text= "Krok zvazku v m").grid(column=0, row=9)
# ttk.Label(frm, text="Počet systémov").grid(column=0, row=10)



#def stoziar_changed(index, value, op):
 #   ax_text.insert('end', str(vypoctove_mapy.stoziare[stoziarCombo.get()].a.x))


#v = StringVar()
#v.trace('w', stoziar_changed)








# zvazokCombo = ttk.Combobox(frm, values=["1","2","3"])
# zvazokCombo.grid(column=2, row=3)
# metodaCombo = ttk.Combobox(frm, values=["Metóda komlexnej hĺbky", "Aproximovaná",])
# metodaCombo.grid(column=2, row=4)
# redukciaCombo = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
# redukciaCombo.grid(column=2, row=5)
# zlozkyCombo = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
# zlozkyCombo.grid(column=2, row=6)
# krokCombo = ttk.Combobox(frm)
# krokCombo.grid(column=2, row=7)
# pocetSystemCombo = ttk.Combobox(frm, state="readonly", values=["1","2","3","4"])
# pocetSystemCombo.grid(column=2, row=3)
# minvyska = ttk.Combobox(frm)
# minvyska.grid(column=2, row=4)









def vypocitaj_pressed():
    stoziar = vypoctove_mapy.stoziare[stoziarCombo.get()]
    stoziar.a.x = float(ax_text.get("1.0",END))
    fvodic = vypoctove_mapy.vodice[fvodicCombo.get()]
    zvodic = vypoctove_mapy.vodice[zvodicCombo.get()]


    if metodaCombo.get() == "Aproximovaná":  

        Z = vypoctove_metody.aproximovana_metoda(fvodic, stoziar)
        Zabc = Kronova_redukcia.kronovaRedukcia(Z)
        Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)
       


    if metodaCombo.get() == "Metóda komlexnej hĺbky":    
        result = vypoctove_metody.metoda_komplexnej_hlbky(fvodic, stoziar)            

   
    
    #result vypises do grafickeho okna



vypocitaj = ttk.Button(text="Vypočítaj", command=vypocitaj_pressed).grid()

def debug_pressed():
    root = Tk()
    root.geometry()
    root.title("ahoj")
    messagebox.showinfo("debug", stoziarCombo["values"])

debug = ttk.Button(text="Debug", command=debug_pressed).grid()

root.mainloop()

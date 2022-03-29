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
#root2 = Tk()                             #Druhý rámík
frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(root2, padding=10)

frm.grid(row=0)
#frm2.grid(row=1)

ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)
ttk.Label(frm, text="Typ fázového vodiča").grid(column=0, row=1)
ttk.Label(frm, text="Typ vodiča zemného lana").grid(column=0, row=2)
ttk.Label(frm, text = "Počet vodičov vo zväzku").grid(column=0, row=3)
ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=4)
ttk.Label(frm, text= "Kronova redukcia").grid(column=0, row=5)
ttk.Label(frm, text= "Zlozkova sustava").grid(column=0, row=6)
ttk.Label(frm, text= "Krok zvazku v m").grid(column=0, row=7)
# ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
# ttk.Label(frm, text="Minimálna výška vodiča (m)").grid(column=0, row=4)





stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.stoziare.keys()))        
stoziarCombo.grid(column=2, row=0)
fvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()))
fvodicCombo.grid(column=2, row=1)
zvodicCombo = ttk.Combobox(frm, state="readonly", values=list(vypoctove_mapy.vodice.keys()))
zvodicCombo.grid(column=2, row=2)
zvazokCombo = ttk.Combobox(frm, values=["1","2","3"])
zvazokCombo.grid(column=2, row=3)
metodaCombo = ttk.Combobox(frm, values=["Metóda komlexnej hĺbky", "Aproximovaná",])
metodaCombo.grid(column=2, row=4)
redukciaCombo = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
redukciaCombo.grid(column=2, row=5)
zlozkyCombo = ttk.Combobox(frm, state="readonly", values=["áno","nie"])
zlozkyCombo.grid(column=2, row=6)
krokCombo = ttk.Combobox(frm)
krokCombo.grid(column=2, row=7)
# pocetSystemCombo = ttk.Combobox(frm, state="readonly", values=["1","2","3","4"])
# pocetSystemCombo.grid(column=2, row=3)
# minvyska = ttk.Combobox(frm)
# minvyska.grid(column=2, row=4)









def vypocitaj_pressed():
    stoziar = vypoctove_mapy.stoziare[stoziarCombo.get()]
    stoziar.a.x = 16
    stoziar.a.y = -10
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

# def debug_pressed():
#     messagebox.showinfo("debug", stoziarCombo["values"])

# debug = ttk.Button(text="Debug", command=debug_pressed).grid()
root.mainloop()


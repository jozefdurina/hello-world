from tkinter import *
from tkinter import ttk
import copy
import numpy
import matplotlib.pyplot as plt
from pyparsing import col

from XY import XY
from Vodic import Vodic
from Stoziar import System, ZemneLano, Stoziar
import Aproximovana_metoda
import Kronova_redukcia
import Zlozkova_sustava



vodice = {                                           ##KSI TREBA ZMENIT!!! - NEPLATNE
    "476-AL1/62-ST1A"     : Vodic(D=30.2, RDC20=0.0608, ksi=0.7788, pocet_vo_zvazku=3),
    "243-AL1/39-ST1A"     : Vodic(D=21.8, RDC20=0.1188, ksi=0.7788, pocet_vo_zvazku=1),
    "121-AL4/66-A20SA"    : Vodic(D=18.2, RDC20=0.229, ksi=0.7788, pocet_vo_zvazku=1),
    "178-AL3/53-A20SA"    : Vodic(D=20.4, RDC20=0.167, ksi=0.7788, pocet_vo_zvazku=1),
}

stoziare = {
    "2x400kV Donau N+0" : Stoziar (
        [
            System ( XY (-8.25, 18.24 ), XY (-14.7, 18.24 ), XY ( -10.8, 29.45 ) ),
            System ( XY ( 8.25, 18.24 ), XY ( 14.7, 18.24 ), XY (  10.8, 29.45 ) ), 
        ], 
        [
            ZemneLano(XY(-12.10, 36.45)), 
            ZemneLano(XY( 12.10, 36.45)),
        ],
        vodice["476-AL1/62-ST1A"],  #typ fazovych vodicov
        vodice["178-AL3/53-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "2x400kV Sudok N+0" : Stoziar (
        [
            System ( XY ( -7.5, 19 ), XY ( -9.1, 28 ), XY ( -7.1, 45.6 ) ),
            System ( XY (  7.5, 19 ), XY (  9.1, 28 ), XY (  7.1, 45.6 ) ),
        ], 
        [
            ZemneLano(XY(-5.2, 15)), 
            ZemneLano(XY( 5.2, 15)), 
        ],
        vodice["476-AL1/62-ST1A"],  #typ fazovych vodicov
        vodice["178-AL3/53-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "1x400kV Mačka N+0" : Stoziar (
        [
            System ( XY ( -6.8, 18.6 ), XY ( 0, 27.4 ), XY ( 6.8, 18.6 ) ),
        ], 
        [
            ZemneLano(XY(-3.5, 32.3)), 
            ZemneLano(XY(3.5, 32.3)), 
        ],
        vodice["476-AL1/62-ST1A"],  #typ fazovych vodicov
        vodice["178-AL3/53-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "1x400kV Portal N+0" : Stoziar (
        [
            System ( XY ( -11, 18.2 ), XY ( 0, 18.2 ), XY ( 11, 18.2 ) ),
        ], 
        [
            ZemneLano(XY(-5.5, 31.03)), 
            ZemneLano(XY( 5.5, 31.03)), 
        ],
        vodice["476-AL1/62-ST1A"],  #typ fazovych vodicov
        vodice["178-AL3/53-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "2x110kV Sudok N+0" : Stoziar (
        [
            System ( XY ( -3.03, 14.99 ), XY ( -3.83, 18.84 ), XY ( -3.03, 22.69 ) ),
            System ( XY (  3.03, 14.99 ), XY (  3.83, 18.84 ), XY (  3.03, 22.69 ) ),
        ], 
        [
            ZemneLano(XY( 0, 27.89)), 
            
        ],
        vodice["243-AL1/39-ST1A"],  #typ fazovych vodicov
        vodice["121-AL4/66-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "1x110kV F typ N+0" : Stoziar (
        [
            System ( XY ( -3.8, 14.7 ), XY ( 3, 16.6 ), XY ( -3, 18.5 ) ),
        ], 
        [
            ZemneLano(XY(0, 23.6)), 
        ],
        vodice["243-AL1/39-ST1A"],  #typ fazovych vodicov
        vodice["121-AL4/66-A20SA"],  #typ zemneho/zemnych vodica/vodicov
    ),
   
}

root = Tk()
root.title("Výpočet parametrov vedení")


frm = ttk.Frame(root, padding=10)
frm.grid()
frm.grid_rowconfigure(5, minsize=50)
frm.grid_rowconfigure(7, minsize=50)


ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)

def stoziar_changed(index, value, op):
    stoziar = stoziare[stoziarCombo.get()]

    values = []
    popis = ""

    for i in range(len(stoziar.systemy)):
        values.append("SYS" + str(i+1) + " L1 x")
        values.append("SYS" + str(i+1) + " L1 y")
        values.append("SYS" + str(i+1) + " L2 x")
        values.append("SYS" + str(i+1) + " L2 y")
        values.append("SYS" + str(i+1) + " L3 x")
        values.append("SYS" + str(i+1) + " L3 y")

        popis += str(i+1) + ". systém:\n"
        popis += "L1=[" + str(stoziar.systemy[i].L1.x) + ", " + str(stoziar.systemy[i].L1.y) + "]\n" 
        popis += "L2=[" + str(stoziar.systemy[i].L2.x) + ", " + str(stoziar.systemy[i].L2.y) + "]\n"
        popis += "L3=[" + str(stoziar.systemy[i].L3.x) + ", " + str(stoziar.systemy[i].L3.y) + "]\n"

    popis += "Zemné laná: \n"

    for i in range(len(stoziar.zemneLana)):
        values.append("ZL" + str(i+1) + " x")
        values.append("ZL" + str(i+1) + " y")

        popis += "ZL" + str(i+1) + "=[" + str(stoziar.zemneLana[i].ZL.x) + ", " + str(stoziar.zemneLana[i].ZL.y) + "]\n"    

    if stoziar.fvodic.poc_vo_zv > 1:
        values.append("krok zväzku")

    values.append("priehyb")

    

    defaultStoziarParams.config( text = popis)
    

vStoziar = StringVar()
vStoziar.trace('w', stoziar_changed)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()), textvar=vStoziar, width=25) 
stoziarCombo.grid(row=0, column=1)

defaultStoziarParams = ttk.Label(frm, text = "")
defaultStoziarParams.grid(row=0, column=2)


frm.grid_rowconfigure(18, minsize=50)


def vypocitaj_pressed():

    stoziar = copy.deepcopy(stoziare[stoziarCombo.get()])
        
    
    R, L, C, Z = Aproximovana_metoda.aproximovana_metoda(stoziar)

    print("Dalsi vypocet")
    Rabc = Kronova_redukcia.kronovaRedukcia(R, stoziar, "R_redokovana")
    Labc = Kronova_redukcia.kronovaRedukcia(L, stoziar, "L_redukovana")
    print ("C")
    print(C)
    R012 = Zlozkova_sustava.zlozkova_sustava(Rabc, "R_zlozky")
    L012 = Zlozkova_sustava.zlozkova_sustava(Labc, "L_zlozky")
    C012 = Zlozkova_sustava.zlozkova_sustava(C, "C_zlozky")
    
    # print ("Z")
    # print(Z)

    # Zabc = Kronova_redukcia.kronovaRedukcia(Z, stoziar, "Zabc")
    # Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc, "L012")
 
    
ttk.Button(text="Vypocitaj", command=vypocitaj_pressed).grid()


root.mainloop()
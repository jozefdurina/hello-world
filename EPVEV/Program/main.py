from tkinter import *
from tkinter import ttk
import copy
import numpy
import matplotlib.pyplot as plt

from XY import XY
from Vodic import Vodic
from Stoziar import System, ZemneLano, Stoziar
import Aproximovana_metoda



vodice = {                                           ##KSI TREBA ZMENIT!!! - NEPLATNE
    "434-AL1/56-ST1A"   : Vodic(D=28.8, RAC20=0.0666, ksi=0.86, pocet_vo_zvazku=3),
    "moje ZL"   : Vodic(D=28.8, RAC20=0.0666, ksi=0.86, pocet_vo_zvazku=1),
}

stoziare = {
    "2x400kV Donau N+0" : Stoziar (
        [
            System ( XY ( -13.6, 23.24 ), XY ( -7.3, 23.24 ), XY ( -9.6, 34.45 ) ),
            System ( XY (  13.6, 23.24 ), XY (  7.3, 23.24 ), XY (  9.6, 34.45 ) ), 
        ], 
        [
            ZemneLano(XY(-12.10, 36.45)), 
            ZemneLano(XY( 12.10, 36.45)),
        ],
        vodice["434-AL1/56-ST1A"],  #typ fazovych vodicov
        vodice["moje ZL"],  #typ zemneho/zemnych vodica/vodicov
    ),
        "kotevny" : Stoziar (
        [
            System ( XY ( -10, 10 ), XY ( 0, 10 ), XY ( 10, 10 ) ),
        ], 
        [
            ZemneLano(XY(0, 15)), 
        ],
        vodice["434-AL1/56-ST1A"],  #typ fazovych vodicov
        vodice["moje ZL"],  #typ zemneho/zemnych vodica/vodicov
    )
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
    for i in range(len(stoziar.systemy)):
        values.append("SYS" + str(i+1) + " L1 x")
        values.append("SYS" + str(i+1) + " L1 y")
        values.append("SYS" + str(i+1) + " L2 x")
        values.append("SYS" + str(i+1) + " L2 y")
        values.append("SYS" + str(i+1) + " L3 x")
        values.append("SYS" + str(i+1) + " L3 y")

    for i in range(len(stoziar.zemneLana)):
        values.append("ZL" + str(i+1) + " x")
        values.append("ZL" + str(i+1) + " y")

    if stoziar.fvodic.poc_vo_zv > 1:
        values.append("krok zväzku")

    vstup_param['values']=values
    

vStoziar = StringVar()
vStoziar.trace('w', stoziar_changed)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()), textvar=vStoziar, width=25) 
stoziarCombo.grid(column=1, row=0)

ttk.Label(frm, text = "Menený vstupný parameter").grid(column=0, row=17)
frm.grid_rowconfigure(17, minsize=50)

vstup_param = ttk.Combobox(frm, state="readonly", width=25)
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

def analyzuj_pressed():
    stoziar = copy.deepcopy(stoziare[stoziarCombo.get()])
    od = float(rozsah_od.get("1.0",END))
    do = float(rozsah_do.get("1.0",END))
    krokr = float(krok_rozsah.get("1.0",END))
    meneny = vstup_param.get()

    x = numpy.arange(od, do , krokr)
    y = []

    for i in x:
        if meneny == "SYS1 L1 x":
            stoziar.systemy[0].L1.setX(i)            
        elif meneny == "SYS1 L1 y":
            stoziar.systemy[0].L1.setY(i)     
        elif meneny == "SYS1 L2 x":
            stoziar.systemy[0].L1.setX(i)     
        elif meneny == "SYS1 L2 y":
            stoziar.systemy[0].L1.setY(i)
        #doplnit ostatne parametre
        elif meneny == "krok zväzku":
            stoziar.fvodic.set_krokzvazku(i)
        
        stoziar.prepocitaj_m_vzd()  #nutne

        Z = Aproximovana_metoda.aproximovana_metoda(stoziar)
        #Zabc = Kronova_redukcia.kronovaRedukcia(Z)
        #Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)

        y.append(numpy.imag(Z[0][1]))

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    fig.suptitle('Aligning x-axis using sharex')
    ax1.plot(x, y)
    plt.show()

    #import xlsxwriter

    #workbook  = xlsxwriter.Workbook(fvodicCombo.get() + ' ' + zvodicCombo.get() + '.xlsx')
    #worksheet = workbook.add_worksheet()

    # for i in range(len(x)):
    #     worksheet.write(i, 0, x[i])
    #     worksheet.write(i, 1, y[i])




ttk.Button(text="Analyzuj", command=analyzuj_pressed).grid()


root.mainloop()
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



vodice = {                                           ##KSI TREBA ZMENIT!!! - NEPLATNE
    "476-AL1/62-ST1A"     : Vodic(D=30.2, RDC20=0.0608, ksi=0.8, pocet_vo_zvazku=3),
    "243-AL1/39-ST1A"     : Vodic(D=21.8, RDC20=0.1188, ksi=0.8, pocet_vo_zvazku=1),
    "121-AL4/66-A20SA"    : Vodic(D=18.2, RDC20=0.229, ksi=0.8, pocet_vo_zvazku=1),
    "178-AL3/53-A20SA"    : Vodic(D=20.4, RDC20=0.167, ksi=0.8, pocet_vo_zvazku=1),
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
        "1x400kV Macka N+0" : Stoziar (
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
        popis += "L2=[" + str(stoziar.systemy[i].L1.x) + ", " + str(stoziar.systemy[i].L1.y) + "]\n"
        popis += "L3=[" + str(stoziar.systemy[i].L1.x) + ", " + str(stoziar.systemy[i].L1.y) + "]\n"

    popis += "Zemné laná: \n"

    for i in range(len(stoziar.zemneLana)):
        values.append("ZL" + str(i+1) + " x")
        values.append("ZL" + str(i+1) + " y")

        popis += "ZL" + str(i+1) + "=[" + str(stoziar.zemneLana[i].ZL.x) + ", " + str(stoziar.zemneLana[i].ZL.y) + "]\n"

    if stoziar.fvodic.poc_vo_zv > 1:
        values.append("krok zväzku")

    vstup_param['values']=values

    defaultStoziarParams.config( text = popis)
    

vStoziar = StringVar()
vStoziar.trace('w', stoziar_changed)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()), textvar=vStoziar, width=25) 
stoziarCombo.grid(row=0, column=1)

defaultStoziarParams = ttk.Label(frm, text = "")
defaultStoziarParams.grid(row=0, column=2)

ttk.Label(frm, text = "Menený vstupný parameter").grid(row=2, column=0)
frm.grid_rowconfigure(17, minsize=50)

vstup_param = ttk.Combobox(frm, state="readonly", width=25)
vstup_param.grid(column=1, row=2)

ttk.Label(frm, text="rozsah od",  width=10, anchor = "e").grid(row=3, column=3)
rozsah_od = Text(frm, height=1, width=7)
rozsah_od.grid(column=4, row=3)

ttk.Label(frm, text="rozsah do",  width=10, anchor = "e").grid(row=3, column=5)
rozsah_do = Text(frm, height=1, width=7)
rozsah_do.grid(column=6, row=3)

ttk.Label(frm, text="krok rozsahu",  width=10, anchor = "e").grid(row=3, column=7)
krok_rozsah= Text(frm, height=1, width=7)
krok_rozsah.grid(column=8, row=3)

frm.grid_rowconfigure(18, minsize=50)

def analyzuj_pressed():
    stoziar = copy.deepcopy(stoziare[stoziarCombo.get()])   #robim kopiu, aby som nemenil defaultne hodnoty stoziarov
    od = float(rozsah_od.get("1.0",END))
    do = float(rozsah_do.get("1.0",END))
    krokr = float(krok_rozsah.get("1.0",END))
    meneny = vstup_param.get()

    x = numpy.arange(od, do , krokr)
    y1 = []
    y2 = []
    y3 = []

    for i in x:
        if meneny == "SYS1 L1 x":
            stoziar.systemy[0].L1.setX(i)            
        elif meneny == "SYS1 L1 y":
            stoziar.systemy[0].L1.setY(i)     
        elif meneny == "SYS1 L2 x":
            stoziar.systemy[0].L2.setX(i)     
        elif meneny == "SYS1 L2 y":
            stoziar.systemy[0].L2.setY(i)
        elif meneny == "SYS1 L3 x":
            stoziar.systemy[0].L3.setX(i)            
        elif meneny == "SYS1 L3 y":
            stoziar.systemy[0].L3.setY(i)     
        elif meneny == "SYS2 L1 x":
            stoziar.systemy[1].L1.setX(i)            
        elif meneny == "SYS2 L1 y":
            stoziar.systemy[1].L1.setY(i)     
        elif meneny == "SYS2 L2 x":
            stoziar.systemy[1].L2.setX(i)     
        elif meneny == "SYS2 L2 y":
            stoziar.systemy[1].L2.setY(i)
        elif meneny == "SYS2 L3 x":
            stoziar.systemy[1].L3.setX(i)            
        elif meneny == "SYS2 L3 y":
            stoziar.systemy[1].L3.setY(i)     
        #zemne lana
        elif meneny == "ZL1 x":
            stoziar.zemneLana[0].setX(i)            
        elif meneny == "ZL1 y":
            stoziar.zemneLana[0].setY(i)     
        elif meneny == "ZL2 x":
            stoziar.zemneLana[1].setX(i)            
        elif meneny == "ZL2 y":
            stoziar.zemneLana[1].setY(i)    
        #krok zvazku pre 400kV
        elif meneny == "krok zväzku":
            stoziar.fvodic.set_krokzvazku(i)
        
        stoziar.prepocitaj_m_vzd()  #nutne

        Z = Aproximovana_metoda.aproximovana_metoda(stoziar)
        Zabc = Kronova_redukcia.kronovaRedukcia(Z, stoziar)
        #Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc)

        y1.append(numpy.real(Zabc[0][0])) 
        y2.append(numpy.real(Zabc[1][1]))
        y3.append(numpy.real(Zabc[2][2]))

    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    fig.suptitle('Aligning x-axis using sharex')
    ax1.plot(x, y1)
    ax2.plot(x, y2)
    ax3.plot(x, y3)
    plt.show()

    #import xlsxwriter

    #workbook  = xlsxwriter.Workbook(fvodicCombo.get() + ' ' + zvodicCombo.get() + '.xlsx')
    #worksheet = workbook.add_worksheet()

    # for i in range(len(x)):
    #     worksheet.write(i, 0, x[i])
    #     worksheet.write(i, 1, y[i])




ttk.Button(text="Analyzuj", command=analyzuj_pressed).grid()


root.mainloop()
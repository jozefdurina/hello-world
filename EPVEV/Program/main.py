from ctypes import alignment
from tkinter import *
from tkinter import ttk
import copy
from turtle import left
import numpy
import matplotlib.pyplot as plt
from pyparsing import col
from XY import XY
from Vodic import Vodic, ZvazkovyVodic
from Stoziar import System, ZemneLano, Stoziar
import Aproximovana_metoda
import Kronova_redukcia
import Zlozkova_sustava
import xlsxwriter



vodice = {                                           ##KSI TREBA ZMENIT!!! - NEPLATNE
    "476-AL1/62-ST1A"     : ZvazkovyVodic(D=30.2, RDC20=0.0608, ksi=0.7788),
    "243-AL1/39-ST1A"     : Vodic(D=21.8, RDC20=0.1188, ksi=0.7788),
    "121-AL4/66-A20SA"    : Vodic(D=18.2, RDC20=0.229, ksi=0.7788),
    "178-AL3/53-A20SA"    : Vodic(D=20.4, RDC20=0.167, ksi=0.7788),
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
root.title("EPVEV-Výpočet a analýza parametrov vedení")


frm = ttk.Frame(root, padding=10)
frm.grid()
frm.grid_rowconfigure(5, minsize=50)
frm.grid_rowconfigure(7, minsize=50)


ttk.Label(frm, text="Typ stožiara").grid(column=0, row=0)

def stoziar_changed(index, value, op):
    stoziar = stoziare[stoziarCombo.get()]

    values = []

    values.append("priemer FV")
    values.append("priemer ZL")
    values.append("priehyb")
    
    if stoziar.fvodic.poc_vo_zv > 1:
        values.append("krok zväzku")

    vstup_param['values']=values
 
    popis = "Priemer FV = " + str(stoziar.fvodic.D * 1000) + "mm\n"
    popis += "Priemer ZL = " + str(stoziar.zvodic.D * 1000) + "mm\n"
    if stoziar.fvodic.poc_vo_zv > 1:
        popis += "Krok zväzku = 0.4m"

    defaultStoziarParams.config( text = popis)
    

vStoziar = StringVar()
vStoziar.trace('w', stoziar_changed)

stoziarCombo = ttk.Combobox(frm, state="readonly", values=list(stoziare.keys()), textvar=vStoziar, width=25) 
stoziarCombo.grid(row=0, column=1)

defaultStoziarParams = ttk.Label(frm, text = "")
defaultStoziarParams.grid(row=5, column=1)

ttk.Label(frm, text = "Menený vstupný parameter").grid(row=1, column=0)
frm.grid_rowconfigure(10, minsize=50)

vstup_param = ttk.Combobox(frm, state="readonly", width=25)
vstup_param.grid(column=1, row=1)

ttk.Label(frm, text="rozsah od",  width=10, anchor = "e").grid(row=2, column=0)
rozsah_od = Text(frm, height=1, width=7)
rozsah_od.grid(column=1, row=2)

ttk.Label(frm, text="rozsah do",  width=10, anchor = "e").grid(row=3, column=0)
rozsah_do = Text(frm, height=1, width=7)
rozsah_do.grid(column=1, row=3)

ttk.Label(frm, text="krok rozsahu",  width=10, anchor = "e").grid(row=4, column=0)
krok_rozsah= Text(frm, height=1, width=7)
krok_rozsah.grid(column=1, row=4)

frm.grid_rowconfigure(10, minsize=50)

def analyzuj_pressed():
    
    od = float(rozsah_od.get("1.0",END))
    do = float(rozsah_do.get("1.0",END))
    krokr = float(krok_rozsah.get("1.0",END))
    meneny = vstup_param.get()

    x = numpy.arange(od, do + krokr , krokr)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []

    for i in x:
        stoziar = copy.deepcopy(stoziare[stoziarCombo.get()])   #robim kopiu, aby som nemenil defaultne hodnoty stoziarov
        
        if meneny == "priemer FV":
            stoziar.fvodic.set_D(i)
        if meneny == "priemer ZL":
            stoziar.zvodic.set_D(i)
        elif meneny == "krok zväzku":
            stoziar.fvodic.set_krok_zvazku(i)
        elif meneny == "priehyb":
            stoziar.posunDole(i*2/3)    #priemerna vyska vodica sa pocita ako 2/3 z priehybu 
            stoziar.prepocitaj_m_vzd()  #nutne
            stoziar.prepocitaj_m_vzd_obrazov() #nutne


        R, L, C, Z = Aproximovana_metoda.aproximovana_metoda(stoziar)
    
        #print(stoziar_changed.stoziar)
        Rabc = Kronova_redukcia.kronovaRedukcia(R, stoziar, "R_redukovana")
        Labc = Kronova_redukcia.kronovaRedukcia(L, stoziar, "L_redukovana")
        print ("C")
        print(C)
        R012 = Zlozkova_sustava.zlozkova_sustava(Rabc, "R_zlozky")
        L012 = Zlozkova_sustava.zlozkova_sustava(Labc, "L_zlozky")
        C012 = Zlozkova_sustava.zlozkova_sustava(C, "C_zlozky")
              
        Zabc = Kronova_redukcia.kronovaRedukcia(Z, stoziar, "Z_redukovana")
        Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc, "Z_zlozky")



        y1.append(numpy.real(Z012[0][0]))                  #nulova zlozka rezistancie
        y2.append(numpy.real(Z012[1][1]))                  #susledna zlozka rezistancie
        y3.append(numpy.real(L012[0][0]))                  #nulova zlozka induktancie                                  
        y4.append(numpy.real(L012[1][1]))                  #susledna zlozka induktancie
        y5.append(numpy.real(C012[0][0]))                  #nulova zlozka kapacitancie
        y6.append(numpy.real(C012[1][1]))                  #susledna zlozka kapacitancie

   
    

    fig, ax = plt.subplots(figsize=(13,8))         #deklaruje že fig a ax su subplots
    fig.subplots_adjust(right=0.8, left= 0.05)  # posun pravej osi y prvej plochy do 3/4 okna
    fig.suptitle(stoziarCombo.get() + '_' + vstup_param.get() + '_' + str(od) + '_' + str(do) + '_' + str(krokr), fontsize=14)
   
    twin1 = ax.twinx()
    twin2 = ax.twinx()


    # Offset the right spine of twin2.  The ticks and label have already been
    # placed on the right by twinx above.
    twin2.spines.right.set_position(("axes", 1.15))  # twin2 pravu os y posuva na poziciu 1.2 o 1.0 osi x - 1.4 už nie je v okne vidieť

    p1, = ax.plot(x, y1, "b-", label="R0 - nulova zlozka rezistancie")   # , je dolezita neviem preco
    p2, = ax.plot(x, y2, "b--", label="R1 - susledna zlozka rezistancie")   
    p3, = twin1.plot(x, y3, "r-", label="L0 - nulova zlozka induktancie")
    p4, = twin1.plot(x, y4, "r--", label="L1 - susledna zlozka induktancie")
    p5, = twin2.plot(x, y5, "g-", label="C0 - nulova zlozka kapacitancie")
    p6, = twin2.plot(x, y6, "g--", label="C1 - susledna zlozka kapacitancie")

    ax.set_xlim()
    ax.set_ylim(0, (max(max(y1), max(y2)))*1.05)
    twin1.set_ylim(0, (max(max(y3), max(y4)))*1.1)
    twin2.set_ylim(0, (max(max(y5), max(y6)))*1.15)

    if vstup_param.get() == "priemer FV":
        ax.set_xlabel("priemer FV (mm)")
    elif vstup_param.get() == "priemer ZL":   
        ax.set_xlabel("priemer ZL (mm)")
    elif vstup_param.get() == "krok zväzku": 
        ax.set_xlabel("krok zväzku (m)") 
    elif vstup_param.get() == "priehyb": 
        ax.set_xlabel("priehyb (m)") 


    ax.set_ylabel("R (ohm/km)")
    twin1.set_ylabel("L (H/km)")
    twin2.set_ylabel("C (F/km)")
    

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p3.get_color())
    twin2.yaxis.label.set_color(p5.get_color())


    tkw = dict(size=4, width=1.5)                              #okno
    ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
    twin1.tick_params(axis='y', colors=p3.get_color(), **tkw)
    twin2.tick_params(axis='y', colors=p5.get_color(), **tkw)
    ax.tick_params(axis='x', **tkw)

    ax.legend(handles=[p1,p2,p3,p4,p5,p6],loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=3) 
    

    plt.show()
    
    workbook  = xlsxwriter.Workbook(stoziarCombo.get() + '_' + vstup_param.get() + '_' + str(od) + '_' + str(do) + '_' + str(krokr) +'.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 6, 13.0)
    format1 = workbook.add_format()
    format1.set_align("center") 
    format1.set_bold()
    format2 = workbook.add_format()
    format2.set_align("center") 


    worksheet.write(0, 0, stoziarCombo.get() + '_' + vstup_param.get(), format1)
    if vstup_param.get() == "priemer FV":
        worksheet.write(1, 0, "priemer FV)", format1)
        worksheet.write(2, 0, "(mm)", format1)
    elif vstup_param.get() == "priemer ZL":   
        worksheet.write(1, 0, "priemer ZL", format1)
        worksheet.write(2, 0, "(mm)", format1)
    elif vstup_param.get() == "krok zväzku": 
        worksheet.write(1, 0, "krok zväzku", format1)
        worksheet.write(2, 0, "(m)", format1)
    elif vstup_param.get() == "priehyb": 
        worksheet.write(1, 0, "priehyb", format1)
        worksheet.write(2, 0, "(m)", format1)
     
    worksheet.write(1, 1, "R0", format1)
    worksheet.write(2, 1, "(ohm/km)", format1)
    worksheet.write(1, 2, "R1", format1)
    worksheet.write(2, 2, "(ohm/km)", format1)
    worksheet.write(1, 3, "L0", format1)
    worksheet.write(2, 3, "(H/km)", format1)
    worksheet.write(1, 4, "L1", format1)
    worksheet.write(2, 4, "(H/km)", format1)
    worksheet.write(1, 5, "C0", format1)
    worksheet.write(2, 5, "(F/km)", format1)
    worksheet.write(1, 6, "C1", format1)
    worksheet.write(2, 6, "(F/km)", format1)

    for i in range(len(x)):  
        worksheet.write(i+3, 0, x[i], format2)
        worksheet.write(i+3, 1, y1[i], format2)
        worksheet.write(i+3, 2, y2[i], format2)
        worksheet.write(i+3, 3, y3[i], format2)
        worksheet.write(i+3, 4, y4[i], format2)
        worksheet.write(i+3, 5, y5[i], format2)
        worksheet.write(i+3, 6, y6[i], format2)

    
    workbook.close()
    

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
    Zabc = Kronova_redukcia.kronovaRedukcia(Z, stoziar, "Z_redukovana")
    Z012 = Zlozkova_sustava.zlozkova_sustava(Zabc, "Z_zlozky")
 
    

    #workbook  = xlsxwriter.Workbook(stoziarCombo.get() +'.xlsx')
    #worksheet = workbook.add_worksheet()

    # for i in range(stoziar.pocetFazvychVodicov()):
    #     worksheet.write(1+i, 1, numpy.real(Z012[i][0]))
    #     worksheet.write(1+i, 2, numpy.imag(Z012[i][0]))
    #     worksheet.write(1+i, 3, str(numpy.real(Z012[i][0])) + "+" + str(numpy.imag(Z012[i][0])) + "i" )

    # worksheet.write(9, 0, "Matica Z012")
    # for i in range(len(Z012)):
    #     for j in range(len(Z012[i])):
    #         worksheet.write(10+i, j, str(numpy.real(Z012[i][j])) + "+" + str(numpy.imag(Z012[i][j])) + "i" )

    # worksheet.write(9, 0, "Matica R012")
    # for i in range(len(Z012)):
    #     for j in range(len(Z012[i])):
    #         worksheet.write(10+i, j, str(numpy.real(Z012[i][j]))) 

    # worksheet.write(9, 5, "Matica L012")
    # for i in range(len(Z012)):
    #     for j in range(len(Z012[i])):
    #         worksheet.write(10+i, 5+j, str(numpy.imag(Z012[i][j])))       

    # workbook.close()


ttk.Button(text="Vypocitaj", command=vypocitaj_pressed).grid()
ttk.Button(text="Analyzuj", command=analyzuj_pressed).grid()


root.mainloop()
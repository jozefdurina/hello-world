from tkinter import *
from tkinter import ttk
import tkinter as tk
from unicodedata import name

root = Tk()
#root2 = Tk()                             #Druhý rámík
frm = ttk.Frame(root, padding=10)
#frm2 = ttk.Frame(root, padding=10)

frm.grid(row=0)
#frm2.grid(row=1)


ttk.Label(frm, text="Portál").grid(column=0, row=0)
ttk.Label(frm, text="Fázový vodič").grid(column=0, row=1)
ttk.Label(frm, text="Vodič zemného lana").grid(column=0, row=2)
ttk.Label(frm, text="Počet systémov").grid(column=0, row=3)
ttk.Label(frm, text="Minimálna výška vodiča").grid(column=0, row=4)
ttk.Label(frm, text="Kronova redukcia").grid(column=0, row=5)
ttk.Label(frm, text="Metóda výpočtu").grid(column=0, row=6)


#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=3)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=7)
ttk.Button(text="Vypočítaj").grid()
ttk.Button(text="Vypočítaj 2").grid()

Portál="akalsk"


Vodič = "aa"
labelTop = tk.Label(frm, text = "Počet vodičov vo zväzku")
labelTop.grid(column=0, row=7)


Portál = ttk.Combobox(frm, values=[
                                    "Kotevný", 
                                    "Kotevný rozkročený",
                                    "Kotevný typ 1",
                                    "Kotevný typ 2 užší povodný",
                                    "Kotevný typ 3 širší povodný",
                                    "Nosný uzky",
                                    "Nosný rozkročený"])
#print(dict(Portál))                           #čo je dict??                
Portál.grid(column=2, row=0)
Portál.current(0)

print(Portál.current(), Portál.get())


ttk.Combobox(frm, values=["185  AlFe 3",
"185  AlFe 6",
"185  AlFe 3",
"240  AlFe 6",
"350  AlFe 4",
"350  AlFe 6",
"450  AlFe 6",
"450  AlFe 8",
"500  AlFe 8",
"670  AlFe 8",]).grid(column=2, row=1)


ttk.Combobox(frm, values=["185  AlFe 3",
"185  AlFe 6",
"185  AlFe 3",
"240  AlFe 6",
"350  AlFe 4",
"350  AlFe 6",
"450  AlFe 6",
"450  AlFe 8",
"500  AlFe 8",
"670  AlFe 8",]).grid(column=2, row=2)

ttk.Combobox(frm, values=["1",
"2",
"3",
"4"]).grid(column=2, row=3)
ttk.Combobox(frm, values=["aaa"]).grid(column=2, row=4)
ttk.Combobox(frm, values=["áno",
"nie"]).grid(column=2, row=5)
ttk.Combobox(frm, values=["Metóda komlexnej hlbky",
"Metóda Alvardo",
"Metóda 3",]).grid(column=2, row=6)
ttk.Combobox(frm, values=["1",
"2",
"3",
"4"]).grid(column=2, row=7)


root.mainloop()


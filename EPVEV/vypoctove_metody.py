import math
import cmath
from typing import runtime_checkable
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def metod_soZL( stoziar, fvodic, zvodic ):
    pass

def metoda_bezZL( stoziar, fvodic ):

    u_0=4*math.pi*pow(10,-7)*1000 #permeabilita vakua, Henri/meter
    u_rg=1                    #relet9vna permeabilita zeme, -
    u_g=u_rg*u_0               #permeabilita zeme,  Henri/meter

    e_0=8.854*pow(10,-12) *1000      #permitivita vakua, Farad/meter
    e_rg=15                      #relativna permitivita zeme, - 
    e_g=e_rg*e_0                   #permitivita zeme, Farad/meter

    rho_g=100
    s_g=1/rho_g                    #konduktivita zeme, Siemens/meter 

    f=50
    w=2*math.pi*f               #uhlova rychlost, Radian/s

    r_c=0.0268/2                  #polomer vodica, meter

    g_0=w*pow(u_0*e_0, 1/2)*1j          #koeficient sirenia vlny vo vaku, 1/meter
    g_g=pow((w*u_g*(s_g+w*e_g*1j))*1j, 1/2)     #koeficient sirenia vlny v zemi, 1/meter

    p_g=pow(g_g,-1)                         #komplexna hlbka vniku v zemi, meter

    p_komplexnahlbka=pow(rho_g/(w*u_g*1j),1/2)

    xi=0.8212

    R_ac=0.0888

    dim=[[-12,18.799],
        [0,18.799],
        [12,18.799],
        [-6,31.789],
        [6,31.789]]            #suradnice stoziara, m
    n_k=len(dim)                                                    #pocet vodicov
    

    Z=[[0 for i in range (0, n_k)] for j in range (0, n_k)]   #impedancia
    D=[[0 for i in range (0, n_k)] for j in range (0, n_k)]
    d=[[0 for i in range (0, n_k)] for j in range (0, n_k)]
    Di=[[0 for i in range (0, n_k)] for j in range (0, n_k)]


    for i in range (0,n_k):
        for j in range (0,n_k):
            d[i][j]=(dim[j][0]-dim[i][0])
            D[i][j]=pow(pow(dim[j][1]+dim[i][1],2)+pow(d[i][j],2),1/2)
            Di[i][j]=pow(pow(dim[j][1]-dim[i][1]+2*p_komplexnahlbka,2)+pow(d[i][j],2),1/2)
            if i==j:
                Z[i][j]=R_ac+1j*w*(u_0/(2*math.pi)*cmath.log((2*(dim[i][1]+p_komplexnahlbka)/(xi*r_c))))  ##*1000??
            else : 
                Z[i][j]=1j*w*(u_0/(2*math.pi)*cmath.log((Di[i][j]/D[i][j])))


    for i in range (0,n_k):
        print(d[i])
    print()

    for i in range (0,n_k):
        print(D[i])
    print()

    print("Matica Di:")
    for i in range (0,n_k):
        print(Di[i])
    print()

    for i in range (0,n_k):
        print(Z[i])
    print()

    print('-----------------------------------------------')

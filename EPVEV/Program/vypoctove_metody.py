import math
import cmath
import main

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
    #Rii = fvodic.rdc20 + Rg

    

    if main.zvazokCombo.get() == "1":
       
        Er = fvodic.E * r
        Rii = fvodic.rdc20 + Rg

    if main.zvazokCombo.get() == "2":
        p=main.krokCombo.get()/(2*sin(math.pi/2))     #polomer kruznice rozmiestnenia vodicov vo zvazku
        r_zv=sqrt((2*r*pow(p,1)),2)
        Er= sqrt(E*r_zv, 2)


    L = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    
    R = [
        [0,0,0,0,0], 
        [0,0,0,0,0],
        [0,0,0,0,0], 
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]


    Z = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

    for i in range(5):
        for k in range(5):
            if i==k:
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/(Er), math.e)   #zistit ci treba r
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

    return Z


#def metoda_komplexnej_hlbky(fvodic, stoziar):
#     u_0=4*math.pi*pow(10,-7) #permeabilita vakua, Henri/meter
#     u_rg=1                    #relet9vna permeabilita zeme, -
#     u_g=u_rg*u_0               #permeabilita zeme,  Henri/meter

#     e_0=8.854*pow(10,-12)     #permitivita vakua, Farad/meter
#     e_rg=15                      #relativna permitivita zeme, - 
#     e_g=e_rg*e_0                   #permitivita zeme, Farad/meter

#     rho_g=100
#     s_g=1/rho_g                    #konduktivita zeme, Siemens/meter 

#     f=50
#     w=2*math.pi*f               #uhlova rychlost, Radian/s

#     #r_c=0.0268/2                   #polomer vodica, meter
#     r_c=fvodic.D/(2*1000)           #polomer vodica, meter

#     g_0=w*pow(u_0*e_0, 1/2)*1j          #koeficient sirenia vlny vo vaku, 1/meter
#     g_g=pow((w*u_g*(s_g+w*e_g*1j))*1j, 1/2)     #koeficient sirenia vlny v zemi, 1/meter

#     p_g=pow(g_g,-1)                         #komplexna hlbka vniku v zemi, meter

#     p_komplexnahlbka=pow(rho_g/(w*u_g*1j),1/2)

#     #xi=0.8260
#     xi=fvodic.E

#     #R_ac=0.1609
#     R_ac = fvodic.RAC20

#     dim=[   #parametre stoziara do vypoctu
#         [stoziar.a.x, stoziar.a.y],
#         [stoziar.b.x, stoziar.b.y],
#         [stoziar.c.x, stoziar.c.y],
#         [stoziar.z1.x, stoziar.z1.y],
#         [stoziar.z2.x, stoziar.z2.y],
#     ]
        
#     n_k=len(dim)                                                    #pocet vodicov
        

#     Z=[[0 for i in range (n_k)] for j in range (n_k)]   #impedancia
#     D=[[0 for i in range (n_k)] for j in range (n_k)]
#     d=[[0 for i in range (n_k)] for j in range (n_k)]
#     Di=[[0 for i in range (n_k)] for j in range (n_k)]


#     for i in range (n_k):
#         for j in range (n_k):
#             d[i][j]=(dim[j][0]-dim[i][0])
#             D[i][j]=pow(pow(dim[j][1]+dim[i][1],2)+pow(d[i][j],2),1/2)
#             Di[i][j]=pow(pow(dim[j][1]-dim[i][1]+2*p_komplexnahlbka,2)+pow(d[i][j],2),1/2)
#             if i==j:
#                 Z[i][j]=R_ac+1j*w*(u_0/(2*math.pi)*cmath.log((2*(dim[i][1]+p_komplexnahlbka)/(xi*r_c))))*1000
#             else : 
#                 Z[i][j]=1j*w*(u_0/(2*math.pi)*cmath.log((Di[i][j]/D[i][j])))*1000


#     for i in range (n_k):
#         print(d[i])
#     print()

#     for i in range (n_k):
#         print(D[i])
#     print()

#     print("Matica Di:")
#     for i in range (n_k):
#         print(Di[i])
#     print()

#     for i in range (n_k):
#         print(Z[i])
#     print()

#     print('-----------------------------------------------')


def vypisMatice(M): # M je matica - definovana ako list listov
    for i in range(len(M)):
        print(M[i])    
    # print("\n")    
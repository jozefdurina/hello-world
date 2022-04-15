import math
import cmath

def aproximovana_metoda(fvodic, zvodic, stoziar):
    D = fvodic.D/1000
    D_z = zvodic.D/1000
    r = D/2
    r_z = D_z/2
    E = fvodic.E
    E_z = zvodic.E
    Rg = 0.049300   #[Ω.km−1]
    mi0 = 4*math.pi*10**-4 #[H/km]
    print(mi0)
    dg = 982.878 #[m]
   # Zik = Rik + jωLik
    Rik = Rg    #[Ω/km]
    Rii = fvodic.rdc20 + Rg
    Rzz = zvodic.rdc20 + Rg


    

    #if main.zvazokCombo.get() == "1":
       
    #     Er = fvodic.E * r
    #     Rii = fvodic.rdc20 + Rg

    # #if main.zvazokCombo.get() == "2":
    #     p=main.krokCombo.get()/(2*sin(math.pi/2))     #polomer kruznice rozmiestnenia vodicov vo zvazku
    #     r_zv=sqrt((2*r*pow(p,1)),2)
    #     Er= sqrt(E*r_zv, 2)


    L = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    
    # R = [
    #     [fvodic.rdc20,Rg,Rg,Rg,Rg], 
    #     [Rg,fvodic.rdc20,Rg,Rg,Rg],
    #     [Rg, Rg, fvodic.rdc20,0,0], 
    #     [Rg,Rg,Rg,zvodic.rdc20,0],
    #     [Rg,Rg,Rg,Rg,zvodic.rdc20]
    # ]

    R = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    Z = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

    for i in range(5):
        for k in range(5):
            if i==k:
                # L[i][k] = (mi0/(2*math.pi)) * math.log(dg/(E*r), math.e)   #zistit ci treba r
                # L[3][3] = (mi0/(2*math.pi)) * math.log(dg/(E_z*r_z), math.e)
                # L[4][4] = (mi0/(2*math.pi)) * math.log(dg/(E_z*r_z), math.e)
                
                if i<3:
                    R[i][i] = Rii
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/(E*r), math.e)   #zistit ci treba r
                    Z[i][k] = Rii+1j*L[i][i]*100*math.pi
                else:
                    R[i][i] = Rzz
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/(E_z*r_z), math.e)
                    Z[i][i] = Rzz+1j*L[i][i]*100*math.pi

                # R[i][k] = Rii
                # R[3][3] = Rzz
                # R[4][4] = Rzz
                # Z[i][k] = Rii+1j*L[i][k]*100*math.pi
                # Z[3][3] = Rzz+1j*L[3][3]*100*math.pi
                # Z[4][4] = Rzz+1j*L[4][4]*100*math.pi
            else:
                R[i][k] = Rik 
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/stoziar.m_vzd[i][k], math.e)                
                Z[i][k] = Rik+1j*L[i][k]*100*math.pi




    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica R\n")
    vypisMatice(R)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica L\n")
    vypisMatice(L)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica Z\n")
    vypisMatice(Z)

    return Z

def vypisMatice(M): # M je matica - definovana ako list listov
    for i in range(len(M)):
        print(M[i])    
    # print("\n")    



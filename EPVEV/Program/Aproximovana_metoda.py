import math

from Stoziar import Stoziar

def aproximovana_metoda(stoziar:Stoziar):

    Rg = 0.049300   #[Ω.km−1]
    mi0 = 4*math.pi*10**-4 #[H/km]
    dg = 982.878 #[m]
    Rik = Rg    #[Ω/km]
    Rii = stoziar.fvodic.RAC20 + Rg
    Rzz = stoziar.zvodic.RAC20 + Rg
  
    rozmer = stoziar.rozmerMaticePreVypocet()

    R = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 
    L = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 
    Z = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 


    for i in range(rozmer):
        for k in range(rozmer):
            if i==k:                
                if i<(len(stoziar.systemy)*3):
                    R[i][i] = Rii
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/(stoziar.fvodic.ksi_r ), math.e)   #zistit ci treba r
                    Z[i][i] = Rii+1j*L[i][i]*100*math.pi
                else:
                    R[i][i] = Rzz
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/(stoziar.zvodic.ksi_r ), math.e)
                    Z[i][i] = Rzz+1j*L[i][i]*100*math.pi

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



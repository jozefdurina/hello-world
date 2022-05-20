import math
import numpy as np
from Stoziar import Stoziar

def aproximovana_metoda(stoziar:Stoziar):

    E0=8.8542*10**-9  #[F/km] 
    Rg = 0.049300   #[Ω.km−1]
    mi0 = 4*math.pi*10**-4 #[H/km]
    dg = 796.039 #[m]
    Rik = Rg    #[Ω/km]
    Rii = stoziar.fvodic.RAC20 + Rg
    Rzz = stoziar.zvodic.RAC20 + Rg
  

    rozmer = stoziar.rozmerMaticePreVypocet()

    R = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 
    L = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 
    Z = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 
    P = [[0 for i in range (0, rozmer)] for j in range (0, rozmer)] 

    vyskyVodicov = []    #vysky vodicov na stoziari nad zemou v poradi najprav vsetky fazove vodice zo systemov a potom zemne vodice
    for i in stoziar.systemy:
        vyskyVodicov.extend([i.L1.y, i.L2.y, i.L3.y])
    for i in stoziar.zemneLana:
        vyskyVodicov.append(i.ZL.y)

    for i in range(rozmer):
        for k in range(rozmer):
            if i==k:                
                if i<(stoziar.pocetFazvychVodicov()):
                    R[i][i] = Rii
                    L[i][i] = (mi0/(2*math.pi)) * math.log((stoziar.fvodic.ksi_r), math.e)   #zistit ci treba r
                    Z[i][i] = Rii+1j*L[i][i]*100*math.pi
                    P[i][i] = (1/(2*math.pi*E0))*np.log((2*vyskyVodicov[i]/stoziar.fvodic.r))
                else:
                    R[i][i] = Rzz
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/(stoziar.zvodic.ksi_r ), math.e)
                    Z[i][i] = Rzz+1j*L[i][i]*100*math.pi
                    P[i][i] = (1/(2*math.pi*E0))*math.log((2*vyskyVodicov[i]/stoziar.zvodic.r))

            else:
                R[i][k] = Rik 
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/stoziar.m_vzd[i][k], math.e)                
                Z[i][k] = Rik+1j*L[i][k]*100*math.pi
                P[i][k] = (1/(2*math.pi*E0))*np.log((stoziar.m_vzd_obrazov[i][k]/stoziar.m_vzd[i][k]))

    C = np.linalg.inv(P)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica R\n")
    vypisMatice(R)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica L\n")
    vypisMatice(L)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica P\n")
    vypisMatice(P)

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica C\n")
    vypisMatice(C)


    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Matica Z\n")
    vypisMatice(Z)

    return Z

def vypisMatice(M): # M je matica - definovana ako list listov
    for i in range(len(M)):
        print(M[i])    
    # print("\n")    



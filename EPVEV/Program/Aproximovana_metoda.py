import math
import numpy as np
from Stoziar import Stoziar

def aproximovana_metoda(stoziar:Stoziar):

    E0=8.8542e-9  #[F/km] 
    Rg = 0.049300   #[Ω.km−1]
    mi0 = math.pi*4e-4 #[H/km]
    dg = 796.039 #[m]
    Rii = stoziar.fvodic.RDC20 + Rg
    Rzz = stoziar.zvodic.RDC20 + Rg
  

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
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/stoziar.fvodic.ksi_r) #zistit ci treba r
                    Z[i][i] = Rii+1j*L[i][i]*100*math.pi
                    P[i][i] = (1/(2*math.pi*E0))*np.log(abs((2*vyskyVodicov[i])/stoziar.fvodic.get_r()))
                else:
                    R[i][i] = Rzz
                    L[i][i] = (mi0/(2*math.pi)) * math.log(dg/stoziar.zvodic.ksi_r)
                    Z[i][i] = Rzz+1j*L[i][i]*100*math.pi
                    P[i][i] = (1/(2*math.pi*E0))*np.log(abs((2*vyskyVodicov[i])/stoziar.zvodic.get_r()))

            else:
                R[i][k] = Rg
                L[i][k] = (mi0/(2*math.pi)) * math.log(dg/stoziar.m_vzd[i][k])                
                Z[i][k] = Rg+1j*L[i][k]*100*math.pi
                P[i][k] = (1/(2*math.pi*E0))*np.log(abs(stoziar.m_vzd_obrazov[i][k]/stoziar.m_vzd[i][k]))

    C = np.linalg.inv(P)

    return R, L, C, Z




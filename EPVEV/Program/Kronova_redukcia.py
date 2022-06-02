import numpy as np
from Stoziar import Stoziar


def kronovaRedukcia(Z, stoziar:Stoziar, popisVysledku):

    pFaz = stoziar.pocetFazvychVodicov()
    pZL = stoziar.pocetZemnychLan()

    Pnn=[[0 for i in range (pFaz)] for j in range (pFaz)]
    for i in range(pFaz):
        for j in range(pFaz):
            Pnn[i][j]=Z[i][j]


    Pnm=[[0 for i in range (pZL)] for j in range (pFaz)]
    for i in range(pFaz):
        for j in range(pZL):
            Pnm[i][j]=Z[i][j+pFaz]


    Pmn=[[0 for i in range (pFaz)] for j in range (pZL)]
    for i in range(pZL):
        for j in range(pFaz):
            Pmn[i][j]=Z[i+pFaz][j]


    Pmm=[[0 for i in range (pZL)] for j in range (pZL)]
    for i in range(pZL):
        for j in range(pZL):
            Pmm[i][j]=Z[i+pFaz][j+pFaz]


    Pabc = np.subtract(Pnn, np.matmul(Pnm, np.matmul(np.linalg.inv(Pmm), Pmn))) 

    print (popisVysledku)
    print(Pabc)

    return Pabc


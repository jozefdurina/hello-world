import numpy as np
from Stoziar import Stoziar


def kronovaRedukcia(Z, stoziar:Stoziar, popisVysledku):

    pFaz = stoziar.pocetFazvychVodicov()
    pZL = stoziar.pocetZemnychLan()

    Pnn=[[0 for i in range (pFaz)] for j in range (pFaz)]
    for i in range(pFaz):
        for j in range(pFaz):
            Pnn[i][j]=Z[i][j]

    # print("Pnn:")
    # print(Pnn)

    Pnm=[[0 for i in range (pZL)] for j in range (pFaz)]
    for i in range(pFaz):
        for j in range(pZL):
            Pnm[i][j]=Z[i][j+pFaz]

    # print("Pnm")
    # print(Pnm)

    Pmn=[[0 for i in range (pFaz)] for j in range (pZL)]
    for i in range(pZL):
        for j in range(pFaz):
            Pmn[i][j]=Z[i+pFaz][j]

    # print("Pmn")
    # print(Pmn)

    Pmm=[[0 for i in range (pZL)] for j in range (pZL)]
    for i in range(pZL):
        for j in range(pZL):
            Pmm[i][j]=Z[i+pFaz][j+pFaz]

    # print("Pmm")
    # print(Pmm)


    Pabc = np.subtract(Pnn, np.matmul(Pnm, np.matmul(np.linalg.inv(Pmm), Pmn))) 

    print (popisVysledku)
    print(Pabc)

    return Pabc

    #PnmPmm=np.multiply(Pnm,Pnn)
    #print(PnmPmm)

import numpy as np


def kronovaRedukcia(M):

    
    Pnn=[[0 for i in range (3)] for j in range (3)]
    for i in range(3):
        for j in range(3):
            Pnn[i][j]=M[i][j]

    # print("Pnn:")
    # print(Pnn)

    Pnm=[[0 for i in range (2)] for j in range (3)]
    for i in range(3):
        for j in range(2):
            Pnm[i][j]=M[i][j+3]

    # print("Pnm")
    # print(Pnm)

    Pmn=[[0 for i in range (3)] for j in range (2)]
    for i in range(2):
        for j in range(3):
            Pmn[i][j]=M[i+3][j]

    # print("Pmn")
    # print(Pmn)

    Pmm=[[0 for i in range (2)] for j in range (2)]
    for i in range(2):
        for j in range(2):
            Pmm[i][j]=M[i+3][j+3]

    # print("Pmm")
    # print(Pmm)


    Pabc = np.subtract(Pnn, np.matmul(Pnm, np.matmul(np.linalg.inv(Pmm), Pmn))) 

    print ("Pabc")
    print(Pabc)

    return Pabc

    #PnmPmm=np.multiply(Pnm,Pnn)
    #print(PnmPmm)

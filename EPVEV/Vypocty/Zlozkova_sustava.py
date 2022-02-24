import numpy as np
import cmath

a=1
a2=2

M=np.array([[0.137+0.719*1j, 0.048+0.280*1j, 0.048+0.236*1j, 0.047+0.269*1j, 0.047+0.242*1j],
   [0.048+0.280*1j, 0.137+0.719*1j, 0.048+0.279*1j, 0.047+0.269*1j, 0.047+0.269*1j],
   [0.048+0.236*1j, 0.048+0.279*1j, 0.137+0.719*1j, 0.047+0.242*1j, 0.047+0.269*1j],
   [0.047+0.269*1j, 0.047+0.269*1j, 0.047+0.242*1j, 0.1354634+0.720581*1j, 0.0444593+0.2811111*1j],
   [0.047+0.242*1j, 0.047+0.269*1j, 0.047+0.269*1j, 0.0466593+0.2811111*1j, 0.1354634+0.720581*1j]
])

T=np.array([[1,1,1],
            [1,a2,a],
            [1,a,a2]
])

T1=np.array((1/3)*[[1,1,1],
            [1,a,a2],
            [1,a2,a]
])

print(T1)
print(cmath.polar(2+3j))
# Pnn=[[0 for i in range (3)] for j in range (3)]
# for i in range(3):
#     for j in range(3):
#         Pnn[i][j]=M[i,j]

# print(Pnn)

# Pnm=[[0 for i in range (2)] for j in range (3)]
# for i in range(3):
#     for j in range(2):
#         Pnm[i][j]=M[i][j+3]

# print(Pnm)

# Pmn=np.array([[0 for i in range (3)] for j in range (2)])
# for i in range(2):
#     for j in range(3):
#         Pmn[i,j]=M[i+3,j]

# print(Pmn)

# Pmm=np.array([[0 for i in range (2)] for j in range (2)])
# for i in range(2):
#     for j in range(2):
#         Pmm[i][j]=M[i+3][j+3]

# print(Pmm)

#PMM=np.linalg.inv(Pmm)
#print(PMM)

#PnmPmm=np.multiply(Pnm,Pnn)
#print(PnmPmm)

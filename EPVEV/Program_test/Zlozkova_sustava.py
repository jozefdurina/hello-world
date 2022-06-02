import math
import numpy as np
import cmath

def zlozkova_sustava(Z, popisVysledku):

   Zlen = len(Z)
   Zabc = []
   
   if (Zlen == 3 or Zlen == 4 or Zlen == 5):
      Zabc = [[0 for i in range (3)] for j in range (3)]
   elif (Zlen == 6 or Zlen == 7 or Zlen == 8):
      Zabc = [[0 for i in range (6)] for j in range (6)]
   
   for i in range(len(Zabc)):
         for j in range(len(Zabc)):
            Zabc[i][j] = Z[i][j]

   a=math.cos(2/3*math.pi) + math.sin(2/3*math.pi)*1j
   a2=math.cos(4/3*math.pi) + math.sin(4/3*math.pi)*1j

   T1=np.array(
      [
         [1, 1,  1 ],
         [1, a2, a ],
         [1, a,  a2]
      ]              
   )

   T1inv=np.multiply ( 1/3, np.array(
      [
         [1, 1 , 1 ],
         [1, a , a2],
         [1, a2, a ] 
      ]
   ))


   T = Tinv = None

   if (len(Zabc)==3):
      T = T1
      Tinv = T1inv
   elif len(Zabc)==6:
      T = [[0 for i in range (6)] for j in range (6)]
      Tinv = [[0 for i in range (6)] for j in range (6)]
      for i in range(3):
         for j in range(3):
            T[i][j] = T1[i][j]
            T[i+3][j+3] = T1[i][j]
            Tinv[i][j] = T1inv[i][j]
            Tinv[i+3][j+3] = T1inv[i][j]

   Z012 = np.matmul( np.matmul(Tinv, Zabc), T)

   print (popisVysledku)
   print(Z012)

   return Z012

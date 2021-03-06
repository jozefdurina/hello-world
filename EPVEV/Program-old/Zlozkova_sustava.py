import math
import numpy as np
import cmath

def zlozkova_sustava(Zabc):

   a=math.cos(2/3*math.pi) + math.sin(2/3*math.pi)*1j
   a2=math.cos(4/3*math.pi) + math.sin(4/3*math.pi)*1j

   T=np.array(
      [
         [1, 1,  1 ],
         [1, a2, a ],
         [1, a,  a2]
      ]
   )

   Tinv=np.multiply ( 1/3, np.array(
      [
         [1, 1 , 1 ],
         [1, a , a2],
         [1, a2, a ] 
      ]
   ))

   Z012 = np.matmul( np.matmul(Tinv, Zabc), T)

   print ("Z012 - zlozkova sustava")
   print(Z012)

   return Z012

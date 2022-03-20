from cmath import cos, sin, sqrt
import math
from numpy import arccos

Uz1=420000
Uz2=15800
Sn=260000000
u_k=13.98
i_0=0.4
dP_k=740000
dP_o=170000


w=2*math.pi*50

#VIN1
Zt= ((u_k/100)*(pow(Uz1,2)/Sn)*0.5)
Rt= dP_k*(pow(Uz1,2)/pow(Sn,2))*0.5
Xt=sqrt(((pow(Zt,2)-pow(Rt,2))))
L1=Xt/w
I_0=(i_0/100)*(Sn/(sqrt(3)*Uz1))
S_0= sqrt(3)*Uz1*I_0
fi_0=arccos(dP_o/S_0)
Z_0=pow(Uz1,2)/S_0
R_m=Z_0/cos(fi_0)
L_m=(Z_0/sin(fi_0))*(1/w)

#VIN2
Zt2= ((u_k/100)*(pow(Uz2,2)/Sn)*0.5)
Rt2= dP_k*(pow(Uz2,2)/pow(Sn,2))*0.5
Xt2=sqrt(((pow(Zt2,2)-pow(Rt2,2))))
L2=Xt2/w
I_0_2=(i_0/100)*(Sn/(sqrt(3)*Uz2))
S_0_2= sqrt(3)*Uz2*I_0_2
fi_0_2=arccos(dP_o/S_0_2)
Z_0_2=pow(Uz2,2)/S_0_2



print("R1")
print(Rt)

print("L1")
print(L1)

print("R2")
print(Rt2)

print("L2")
print(L2)

print("Rm")
print(R_m)

print("Lm")
print(L_m)


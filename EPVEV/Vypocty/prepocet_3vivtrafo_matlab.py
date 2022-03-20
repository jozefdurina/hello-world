import math
from cmath import cos, sin, sqrt
from numpy import arccos, i0


Uz1=400000
Uz2=121000
Uz3=34000
Sn1=200000000
Sn2=200000000
Sn3=100000000
u_k12=15.27
u_k13=14.59
u_k23=7.7
i_0=0.128
dP_k12=450600
dP_k13=200400
dP_k23=220200
dP_0=82200
w=2*math.pi*50

uk12=(u_k12/Sn2)*Sn1
uk13=(u_k13/Sn3)*Sn1
uk23=(u_k23/Sn3)*Sn1

Z12=(uk12/100)*(pow(Uz1,2)/Sn1)
Z13=(uk13/100)*(pow(Uz1,2)/Sn1)
Z23=(uk23/100)*(pow(Uz1,2)/Sn1)

fi12=arccos(dP_k12/((uk12/100)*Sn1))
fi13=arccos(dP_k13/((uk13/100)*Sn1))
fi23=arccos(dP_k23/((uk23/100)*Sn1))

R12=Z12*cos(fi12)
R13=Z13*cos(fi13)
R23=Z23*cos(fi23)

R1=(R12+R13-R23)*0.5
R2=(R12+R23-R13)*0.5
R3=(R13+R23-R12)*0.5

L12=Z12*sin(fi12)/w
L13=Z13*sin(fi13)/w
L23=Z23*sin(fi23)/w

L1=(L12+L13-L23)*0.5
L2=(L12+L23-L13)*0.5
L3=(L13+L23-L12)*0.5

I0=(i_0/100)*(Sn1/(sqrt(3)*Uz1))
S0=sqrt(3)*Uz1*I0
fi0=arccos(dP_0/S0)
Z0=(Uz1**2)/S0
Rm=Z0/cos(fi0)
Lm=(Z0/sin(fi0))*(1/w)

print("R1")
print(R1)
print("R2")
print(R2)
print("R3")
print(R3)
print("L1")
print(L1)
print("L2")
print(L2)
print("L3")
print(L3)
print("Rm")
print(Rm)
print("Lm")
print(Lm)

print(R12)
print(R13)
print(R23)
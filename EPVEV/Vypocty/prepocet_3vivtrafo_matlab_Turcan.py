import math
from cmath import cos, sin, sqrt
from numpy import arccos, i0, imag
#import numpy


def from_polar(radius, angle):
    #prevod z polarnych suradnic na komplexne cislo
    #radius - vzdialenost komplexneho cisla od  (0, 0)
    #angle - uhol v radianoch
    return radius*cos(angle) + radius*sin(angle)*1j


Uz1=400000
Uz2=231000
Uz3=34000
Sn1=500000000
Sn2=500000000
Sn3=180000000
u_k12=13.17
u_k13=38.10
u_k23=60.70
i_0=0.11
dP_k12=776500
dP_k13=562130
dP_k23=848330
dP_0=103880
w=2*math.pi*50

uk12=(u_k12/Sn2)*Sn1
uk13=(u_k13/Sn3)*Sn1
uk23=(u_k23/Sn3)*Sn1

fi12=arccos(dP_k12/((uk12/100)*Sn1))
fi13=arccos(dP_k13/((uk13/100)*Sn1))
fi23=arccos(dP_k23/((uk23/100)*Sn1))


#pre Uz1
Z12_Uz1=(uk12/100)*(pow(Uz1,2)/Sn1)
Z13_Uz1=(uk13/100)*(pow(Uz1,2)/Sn1)
Z23_Uz1=(uk23/100)*(pow(Uz1,2)/Sn1)

#pre Uz2
Z12_Uz2=(uk12/100)*(pow(Uz2,2)/Sn1)
Z13_Uz2=(uk13/100)*(pow(Uz2,2)/Sn1)
Z23_Uz2=(uk23/100)*(pow(Uz2,2)/Sn1)

#pre Uz3
Z12_Uz3=(uk12/100)*(pow(Uz3,2)/Sn1)
Z13_Uz3=(uk13/100)*(pow(Uz3,2)/Sn1)
Z23_Uz3=(uk23/100)*(pow(Uz3,2)/Sn1)

#aaa = from_polar(Z12, fi12)

#Jojo
Z1 = ( from_polar(Z12_Uz1, fi12) + from_polar(Z13_Uz1, fi13) - from_polar(Z23_Uz1, fi23) ) / 2
Z2 = ( from_polar(Z12_Uz2, fi12) + from_polar(Z23_Uz2, fi23) - from_polar(Z13_Uz2, fi13) ) / 2
Z3 = ( from_polar(Z13_Uz3, fi13) + from_polar(Z23_Uz3, fi23) - from_polar(Z12_Uz3, fi12) ) / 2

L11 = imag(Z1) / w
L22 = imag(Z2) / w
L33 = imag(Z3) / w

#Ivo
R12=Z12_Uz1*cos(fi12)
R13=Z13_Uz2*cos(fi13)
R23=Z23_Uz3*cos(fi23)

R1=(R12+R13-R23)*0.5
R2=(R12+R23-R13)*0.5
R3=(R13+R23-R12)*0.5

L12=Z12_Uz1*sin(fi12)/w
L13=Z13_Uz2*sin(fi13)/w
L23=Z23_Uz3*sin(fi23)/w

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
print(Z1.real)
print("L1")
print(L11)
print("R2")
print(Z2.real)
print("L2")
print(L22)
print("R3")
print(Z3.real)
print("L3")
print( L33)
print("Rm")
print(Rm.real)
print("Lm")
print(Lm.real)

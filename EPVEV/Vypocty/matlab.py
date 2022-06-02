import math

D=15                             #[mm]
RDC=28.3e-9                      #[ohm/meter]
A=math.pi*(((D*1e-3)/2)**2)
l=1000                           #[m]

Rii=(RDC*l)/A

print(Rii)

r=D/2/10                        #[cm]  
ur=1

GMR= r*math.e**(-ur/4)

print(GMR)

hi=8                             #[m]
mi0=math.pi*4e-4                 #[H/km]


Li=(mi0/(2*math.pi))       
Lii=Li* math.log((2*hi)/(GMR*1e-2))
print(Lii)

Lik=Li* math.log((16**2+1)**(1/2))
print(Lik)

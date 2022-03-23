from cmath import sqrt
import math


def zvazkovy_vodic(r, a, n)

    r= #polomer vodica v m
    a= #krok zvazku v m
    n= #pocet vodicov vo zvazku


    p=a/(2*sin(math.pi/n))     #polomer kruznice rozmiestnenia vodicov vo zvazku
    r_zv=sqrt((n*r*pow(p,n-1)),n)


return 
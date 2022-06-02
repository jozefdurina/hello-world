import math

class Vodic: 
    def __init__(self, D, RDC20, ksi): #D je v mm
        self.D = D/1000             #self.D je priemer v metroch
        self.r = self.D/2                #polomer v metroch
        self.RDC20 = RDC20          #jednotkovy odpor na km vodica       
        self.ksi = ksi              #parameter lana [bezrozmerny]
        self.ksi_r = self.ksi*self.r     #tato hodnota postupuje do dalsieho vypoctu
        self.poc_vo_zv = 1

    def set_D(self, D): # D je v mm
        self.D = D/1000             #self.D je priemer v metroch
        self.r = self.D/2           #polomer v metroch
        self.ksi_r = self.ksi*self.r

    def get_r(self):
        return self.r


class ZvazkovyVodic:
    #D - priemer jedneho lana vo zvazkovom vodici v mm
    #RDC20 - ohm/km odpor jedneho lana vo zvazku
    #prepokladame iba 3-zvazkovy vodic, nic ine
    def __init__(self, D, RDC20, ksi): #D je v mm
        self.D = D/1000             #self.D je priemer jedneho lana zo zvazku v metroch
        self.r = self.D/2           #polomer jedneho lana zo zvazku v metroch
        self.RDC20 = RDC20 / 3          #jednotkovy odpor na km trojice vodicov - nahradna hodnota
        self.ksi = ksi              #parameter lana [bezrozmerny]
        self.krok_zvazku = 0.4      #uvodny odstup trojvodica v m
        self.poc_vo_zv = 3
        self.prepocitajZvazok()

    #zmena priemeru jedneho lana
    #D v mm
    def set_D(self, D):
        self.D = D/1000             #self.D je priemer v metroch
        self.r = self.D/2           #polomer v metroch
 
        self.prepocitajZvazok()
        
    # a  - vzdialenost medzi dvojicou vodicov v metroch
    def set_krok_zvazku(self, a):
        self.krok_zvazku = a
        self.prepocitajZvazok()

    def get_r(self):    #v metroch
        return self.r_zv

    def prepocitajZvazok(self):
        ro = self.krok_zvazku / ( 2 * ( math.sin ( math.pi / 3 )))
        self.r_zv = (3 * self.r * ( ro ** 2 )) ** ( 1/3 )
        self.ksi_r = self.ksi**(1/3) * self.r_zv

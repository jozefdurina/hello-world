import math

class Vodic: 
    def __init__(self, D, RDC20, ksi, pocet_vo_zvazku): #D je v mm
        self.D = D/1000             #self.D je priemer v metroch
        self.r = self.D/2                #polomer v metroch
        self.RAC20 = RDC20          #jednotkovy odpor na km vodica       
        self.ksi = ksi              #parameter lana [bezrozmerny]
        self.ksi_r = self.ksi*self.r     #tato hodnota postupuje do dalsieho vypoctu
        self.poc_vo_zv = pocet_vo_zvazku
        
        self.set_krokzvazku(0.4)    #defaultna hodnota pre krok zvazku pre zvazkovy Vodic je 0.4 metra

    def set_krokzvazku(self, a):    #a -krok zvazku v metroch
        if self.poc_vo_zv > 1:
            ro=a/(2*(math.sin(math.pi/self.poc_vo_zv)))
            r_zv = (self.poc_vo_zv * self.r * ( ro ** (self.poc_vo_zv - 1 )))**(1/self.poc_vo_zv)
            self.ksi_r = self.ksi**(1/self.poc_vo_zv) * r_zv 
            self.RAC20 = self.RAC20/self.poc_vo_zv

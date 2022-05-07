import XY

class System: 
    def __init(self, L1:XY, L2:XY, L3:XY):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

class ZemneLano:
    def __init__(self, ZL:XY):
        self.ZL = ZL


class Stoziar: 
    #systemy - zoznam systemov na stoziari
    #zemne_lana - zoznam zemnych lan na stoziari
    def __init__(self, systemy, zemne_lana):    
        self.systemy = systemy      #systemy
        self.zl = zemne_lana        #zemne lana
        self.prepocitaj_m_vzd()

    def prepocitaj_m_vzd(self):     
        poradie = []    #poradie suradnic bodov pre vypocet matice vzdialenosti

        for i in range(self.systemy.len()):
            poradie.append(self.systemy[i].L1)
            poradie.append(self.systemy[i].L2)
            poradie.append(self.systemy[i].L3)

        for i in range(self.zemne_lana.len()):
            poradie.append(self.zemne_lana[i].ZL)            

        self.m_vzd = []

        for i in range(poradie.len()):
            riadok = []
            for j in range(poradie.len()):
                vzd = poradie[i].vzd(poradie[j])
                riadok.append(vzd)

            self.m_vzd.append(riadok)    


from XY import XY
from Vodic import Vodic

class System: 
    def __init__(self, L1:XY, L2:XY, L3:XY):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3


class ZemneLano: 
    def __init__(self, ZL:XY):
        self.ZL = ZL


class Stoziar: 
    #systemy - zoznam systemov na stoziari
    #zemne_lana - zoznam zemnych lan na stoziari
    def __init__(self, systemy, zemneLana, fvodic:Vodic, zvodic:Vodic):    
        self.systemy = systemy      #systemy
        self.zemneLana = zemneLana        #zemne lana
        self.fvodic = fvodic
        self.zvodic = zvodic
        self.prepocitaj_m_vzd()

    def rozmerMaticePreVypocet(self):
        return self.pocetFazvychVodicov() + self.pocetZemnychLan()

    def pocetFazvychVodicov(self):
        return 3 * len(self.systemy)

    def pocetZemnychLan(self):
        return len(self.zemneLana)

    def prepocitaj_m_vzd(self):     
        poradie = []    #poradie suradnic bodov pre vypocet matice vzdialenosti

        for i in range(len(self.systemy)):
            poradie.append(self.systemy[i].L1)
            poradie.append(self.systemy[i].L2)
            poradie.append(self.systemy[i].L3)

        for i in range(len(self.zemneLana)):
            poradie.append(self.zemneLana[i].ZL)            

        self.m_vzd = []

        for i in range(len(poradie)):
            riadok = []
            for j in range(len(poradie)):
                vzd = poradie[i].vzd(poradie[j])
                riadok.append(vzd)

            self.m_vzd.append(riadok)   

        return 


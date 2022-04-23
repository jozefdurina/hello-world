import math

class Vodic: 
    def __init__(self, D, RAC20, dFE, prierez, pomer, E, rdc20, t_d):
        self.D = D              #v mm
        self.RAC20 = RAC20
        self.dFE = dFE
        self.prierez = prierez
        self.pomer = pomer
        self.E = E
        self.rdc20 = rdc20
        self.t_d = t_d

    def setD(self, D):
        self.D = D

    def setRAC20(self, RAC20):
        self.RAC20 = RAC20

    def setdFE(self, dFE):
        self.dFE = dFE

    def setprierez(self, prierez):
        self.prierez = prierez

    def setpomer(self, pomer):
        self.pomer = pomer

    def setE(self, E):
        self.E = E

    def setrdc20(self, rdc20):
        self.rdc20 = rdc20
    
    def sett_d(self, t_d):
        self.t_d = t_d

class XY: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vzdialenost(self, bod):
        return math.sqrt((self.x-bod.x)**2 + (self.y-bod.y)**2)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

class Stoziar: 
    def __init__(self, L1:XY, L2:XY, L3:XY, ZL1:XY, ZL2:XY):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.ZL1 = ZL1
        self.ZL2 = ZL2

        self.m_vzd = [
            [ 0               , L1 .vzdialenost(L2), L1 .vzdialenost(L3), L1 .vzdialenost(ZL1), L1 .vzdialenost(ZL2)],
            [ L2.vzdialenost(L1), 0                , L2 .vzdialenost(L3), L2 .vzdialenost(ZL1), L2 .vzdialenost(ZL2)],
            [ L3.vzdialenost(L1), L3 .vzdialenost(L2), 0                , L3 .vzdialenost(ZL1), L3 .vzdialenost(ZL2)],
            [ZL1.vzdialenost(L1), ZL1.vzdialenost(L2), ZL1.vzdialenost(L3), 0                 , ZL1.vzdialenost(ZL2)],
            [ZL2.vzdialenost(L1), ZL2.vzdialenost(L2), ZL2.vzdialenost(L3), ZL2.vzdialenost(ZL1), 0                 ],
        ]





#definicie vypoctovych map

stoziare = {
    "Kotevný"                                : Stoziar(XY(-12.00, 18.799), XY(0, 18.799), XY(12.00, 18.799), XY(-6.0, 31.789), XY(6.0, 31.789)),
    "Kotevný rozkročený"                     : Stoziar(XY(-13.00, 18.736), XY(0, 18.736), XY(13.00, 18.736), XY(-7.0, 31.726), XY(7.0, 31.726)),
    "Kotevný typ 1"                          : Stoziar(XY(-12.00, 18.000), XY(0, 18.000), XY(12.00, 18.000), XY(-6.0, 28.600), XY(6.0, 28.600)),
    "Kotevný typ 3 širší pôvodný "           : Stoziar(XY(-12.63, 18.000), XY(0, 18.000), XY(12.63, 18.000), XY(-6.0, 30.890), XY(6.0, 30.890)),
    "Nosný úzky"                             : Stoziar(XY(-11.00, 18.000), XY(0, 18.000), XY(11.00, 18.000), XY(-5.5, 31.025), XY(5.5, 31.025)),
    "Nosný rozkročený"                       : Stoziar(XY(-12.00, 18.200), XY(0, 18.200), XY(12.00, 18.200), XY(-6.0, 31.025), XY(6.0, 31.025)),
}

vodice = {
    "185  AlFe 3"           :Vodic(20.39, 0.1609, 10.5, 235.60, 3.00, 0.8260, 0.1593, 0.242521),
    "185  AlFe 6"           :Vodic(19.08, 0.1570, 7.08, 214.40, 6.00, 0.8000, 0.1250, 0.314465),
    "240  AlFe 6"           :Vodic(21.35, 0.1263, 7.95, 267.77, 6.00, 0.8000, 0.1250, 0.313817),
    "350  AlFe 4"           :Vodic(26.80, 0.0910, 11.8, 414.40, 3.99, 0.8212, 0.0888, 0.279851),
    "350  AlFe 4 test"      :Vodic(26.80, 0.0888, 11.8, 414.40, 3.99, 0.8212, 0.0888, 0.279851),
}
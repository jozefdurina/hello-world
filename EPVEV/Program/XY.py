import math

class XY: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """geom. vzdialenost bodu s bod"""
    def vzd(self, bod): 
        return math.sqrt((self.x-bod.x)**2 + (self.y-bod.y)**2)

    """vzdialenost bodu s obrazom bod - komplexna hlbka"""
    def vzd_obrazu(self, bod): 
        #mi0 = 4*math.pi*10**-4 #[H/km]
        #ro = 100
        #p = (100/(1j*2*math.pi*50*mi0))**(1/2)
        p=(11.253953951963826-11.253953951963826j)
        
        return ((self.x+bod.x+2*p)**2 + (self.y-bod.y)**2)**(1/2)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

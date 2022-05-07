import math

class XY: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """geom. vzdialenost bodu s bod"""
    def vzd(self, bod): 
        return math.sqrt((self.x-bod.x)**2 + (self.y-bod.y)**2)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

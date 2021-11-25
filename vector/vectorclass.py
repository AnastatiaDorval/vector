import math
class Vector:
    vector = []
    mag = 0
    unitVector = []

    def __init__(self, coordinates):
        self.vector = [num for num in coordinates]

    def findMagnitude(self):
        su = 0
        for num in self.vector:
            su += num**2
        self.mag = math.sqrt(su)

    def findUnitVector(self):
        if self.mag == 0:
            self.findMagnitude()
        else:
            for num in self.vector:
                self.unitVector.append(num/self.mag)
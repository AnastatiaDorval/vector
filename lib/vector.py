import math
class Vector:
    vector = []
    mag = 0

    def __init__(self, coordinates):
        self.vector = [num for num in coordinates]

    def findMagnitude(self):
        su = 0
        for num in self.vector:
            su += num**2
        self.mag = math.sqrt(su)

vec = Vector([3, 5, 7])
vec.findMagnitude()

print("The vector is: {}\n The vector's magnitude is: {}\n".format(vec.vector, vec.mag))
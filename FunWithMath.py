# Starting off
print(22/7)
print(355/113)
import math

print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# experiment with loop above alongside the actual value of Pi. How many
# sides does it take to make the two close?
print(math.pi)
# it takes about 100000000000000000 sides to get close to the value of pi. Yikes!
print(archimedes(100000000000000000))

# modify archimedes function to take the radius of the circle as a parameter
# Can you get a better answer more quickly using a larger circle
def archimedesParameter(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    RadiusS = oneHalfSideS * 1
    polygonCircumference = numSides * RadiusS
    pi = polygonCircumference / 2
    roundUp = round(pi)
    return roundUp
print(archimedesParameter(35))
print(archimedesParameter(1000000000))
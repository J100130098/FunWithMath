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

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
Even = 0
for x in range(1, 101):
    Even = (Even + x * 2)
print(Even)
# compute the sum of the first 50 odd numbers
Odd = 50
for x in range(1, 50):
    Odd = Odd + x * 2
print(Odd)
# compute the average of the first 100 odd numbers
Oavg = 0
for x in range(1, 200):
    if x % 2 :
        Oavg : Oavg + 0
        Oavg = (Oavg + x)
print(Oavg/100)
# write a function that returns the average of the first N numbers, where N is a parameter
Even = 0
for x in range(1, 101):
    Even = (Even + x)
print(Even/101)
# write a function called factorial that computes the product of the first N
#   Numbers, where N is a parameter
factorial = 1
for x in range(1,1000):
    factorial = (factorial * x)
print(factorial)
# Each Number in the Fibonacci sequence is the sum of the previous two numbers
# the first two numbers in the sequence are 1 and 1. compute the 10th Fibbonacci Number, where N is a parameter
# You may assume that N will be greater that or equal to 3.
Fibbonacci = x
for x in range(1,18):
    Fibbonacci = x+x
print(Fibbonacci)

# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# != not equal to

Eggs = 25
print(Eggs == 25)
Coconuts = 15
# compound Boolean expressions
# and both need to be true to be true
# or if either is true, then true
# not is a negative sign
print(not Coconuts < 20)

# Decision making -- selection statements
a = 5
b = 10
c = 75

if a >= b:
    c = 45
    if b>c:
        a=25
    else:
        a = -25
else:
    c=1050
    if b == a:
        c = 25

print(a, b, c)
# this is pretty cool
print(c)
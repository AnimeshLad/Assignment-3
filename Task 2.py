# Task 2: Using the Math Module for Calculations
import math
from math import *
#2.   Uses the math module to calculate the:
       #o   Square root of the number
       #o   Natural logarithm (log base e) of the number
       #o   Sine of the number (in radians)

n = int(input("Enter Number: "))


Square_root = math.sqrt(n)
print(Square_root)

Natural_log = math.log(n)
print(Natural_log)

Sine = math.sin(n)
print(Sine)
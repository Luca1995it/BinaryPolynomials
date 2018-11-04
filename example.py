#!/usr/bin/env python3

from Polynomial.BinPolynomial import BinPolynomial as BP

# 1 + x^2 + x^4
pol1 = BP([1,0,1,0,1])  # from the smaller to the higher degree
print("Polynomial 1", pol1)

# 1 + x + x^2
pol2 = BP([1,1,1])
print("Polynomial 2", pol2)

# SUM (DIFFERENCE HAS NO REAL USE IN THE FIELD OF BITS)
print("Sum", pol1 + pol2)

# PRODUCT
print("Product", pol1 * pol2)

# DIVISION
print("Division", pol1 / pol2)

# MODULE
print("Module", pol1 % pol2)

# POWER
print("Power", pol1 ** 2)

# CHECK EQUALITY EXAMPLE
print("Equality checking", pol2 ** 2 == pol1)

# DEGREE
print("Degree", pol1.deg())

# CREATE POLYNOMIAL FROM INTEGER
pol1 = BP()
pol1.from_int(23) # 23 = 0b10111 -> x^4 + x^2 + x + 1
print("Poly from int", pol1)

# CHECK THAT pol1 IS IRREDUCIBLE
pol1 = BP([1,0,1,0,1])
print(pol1.deg())
# Given that po1 has degree 8, if it is reducible, at least one factor will
# have degree 4 or less.

def isReducible(polynomial):
    import math
    up_to = 2 ** (math.ceil(pol1.deg()/2) + 1)

    for i in range(2, up_to):
        tmp = BP()
        tmp.from_int(i)

        if (pol1 % tmp) == BP([0]):
            return True
    return False

print("Is reducible?", isReducible(pol1))

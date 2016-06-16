import math

def perimeter(s, n):
    """Assumes float inputs and returns the perimeter of a regular polygon"""
    return s*n

def area(s,n):
    """Assumes float inputs and returns the area of a regular polygon"""
    return (0.25*n*(s**2))/(math.tan(math.pi/n))

def SumofAreaandPerSquared(s,n):
    """Assumes float inputs and returns the sum of the area of a regular polygon with the square of its perimeter"""
    total = (float(area(s,n) + (perimeter(s,n))**2))
    print(format(total,'.4f'))
    return total 

n = (int(input("Enter number of sides of polygon: ")))
s = (float(input("Enter length of one side of the polygon: ")))
SumofAreaandPerSquared(s,n)

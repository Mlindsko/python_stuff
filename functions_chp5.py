#####################
#Chapter 5 functions
####################

#most of these functions require math package
import math

#finds area of a circle - area
def area(radius):
    temp = math.pi * radius **2
    return temp

#finds absolute value of a number - absoluteValue
def absoluteValue(x):
    if x < 0:
        return -x
    else:
        return x

#compares magnitude of two integers - comparefunc
def comparefunc(x,y):
    if x > y:
        return 1
    elif x ==  y:
        return 0
    else:
        return -1

#finds the distance between two points - distance
def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy **2
    result = math.sqrt(dsquared)
    return result

#finds the length of a hypotenuse of a right triangle - hypotenuse
def hypotenuse(a,b):
    result = math.sqrt( a**2+b**2)
    return result

#finds the slope of a line between two points - slope
def slope(x1,y1,x2,y2):
    rise = float(y2 -y1)
    run =  float(x2 - x1)
    slope = rise / run
    return slope

#finds the intercept of a line using slope function - intercept
def intercept(x1,y1,x2,y2):
    intercept = y1-slope(x1,y1,x2,y2)*x1
    return intercept

#checks if two intergers are divisible - isDivisible
def isDivisible(x,y):
    return x % y == 0

#checks if an integer is between two numbers - isBetween
def isBetween(x, y, z):
    if x >= y and x <= z:
        return True
    else:
        return False

#returns the factorial of an integer - factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

#returns the fibonacci of a number
def fibonacci (n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

            


from Polynomial import Polynomial
from Polynomial import BestFitPolyFunction
import math
import cmath

def FirstOrderDividedDifference(x0, x1, f):
    return (f(x1) - f(x0)) / (x1 - x0)

def SecondOrderDividedDifference(x0, x1, x2 ,f):
    return (FirstOrderDividedDifference(x1,x2,f) - FirstOrderDividedDifference(x0,x1,f)) / (x2-x0)

def FindRoot(p, x0,x1,x2,ε):
    pass

def Parabola(x0, x1, x2, f):
    return lambda x : f(x2) + (x-x2) * FirstOrderDividedDifference(x2, x1, f) + 
        (x-x2) * (x-x1) * SecondOrderDividedDifference(x2, x1, x0, f)

def W(x0,x1,x2,f):
    return FirstOrderDividedDifference(x2,x1,f) + FirstOrderDividedDifference(x2,x0,f) - 
        FirstOrderDividedDifference(x0,x1)

def NextPoint(x0,x1,x2,f):
    return x2 - (2 * f(x2)) / (W + math.sqrt(W**2 - 4 * f(x2) * SecondOrderDividedDifference(x2,x1,x0,f)))

if __name__ == "__main__":
    # testcases

    #l = [int(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial([-1, -4, 0, 1])
    findRoot(p,-10,-9,-8,1e-7)

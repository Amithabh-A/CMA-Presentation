from Polynomial import Polynomial
from Polynomial import BestFitPolyFunction
import cmath

def FirstOrderDividedDifference(x0, x1, f):
    return (f(x1) - f(x0)) / (x1 - x0)

def SecondOrderDividedDifference(x0, x1, x2 ,f):
    return (FirstOrderDividedDifference(x1,x2,f) - FirstOrderDividedDifference(x0,x1,f)) / (x2-x0)

def FindRoot(p, x0,x1,x2,ε):
    print(abs(p(x2)), ε )
#    j  = 0
    i = 4
    while(abs(p(x2)) > ε):
#        j += 1
#        if(j > 10) : break
        next_x = NextPoint(x0,x1,x2,p)
        print(next_x)
        Show(i, next_x, p)
        x0 = x1
        x1 = x2
        x2 = next_x
        i += 1

def Show(i, x, f):
    if x.imag == 0j:
        x = x.real
        print(str(i) + "\t" + str(round(x, 5)) + "\t\t" + str(round(f(x), 5)))

def Parabola(x0, x1, x2, f):
    return lambda x : f(x2) + (x-x2) * FirstOrderDividedDifference(x2, x1, f) + (x-x2) * (x-x1) * SecondOrderDividedDifference(x2, x1, x0, f)

def W(x0,x1,x2,f):
    return FirstOrderDividedDifference(x2,x1,f) + FirstOrderDividedDifference(x2,x0,f) - FirstOrderDividedDifference(x0,x1,f)

# alternative for calculate_next_x

def NextPoint(x0,x1,x2,f):
    # Why the normal way does not works? 
    q = (x0 - x1) / (x1 - x2) # f [xnm1, xn]
    a = q * f(x0) - q * (1 + q) * f(x1) + q**2 * f(x2)
    b = (2 * q + 1) * f(x0) - (1 + q)**2 * f(x1) + q**2 * f(x2)
    c = (1 + q) * f(x0)
    return x0 - (x0 - x1) * ((2 * c) / (b + cmath.sqrt(b**2 - 4 * a * c)))

#    return x2 - (2 * f(x2)) / (W(x0,x1,x2,f) + cmath.sqrt(W(x0,x1,x2,f)**2 - 4 * f(x2) * SecondOrderDividedDifference(x2,x1,x0,f)))

if __name__ == "__main__":
    # testcases

    #l = [int(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial([-1, -1, -1, 1])
#    print(NextPoint(2,1,0,p))
#    print("before myroot()")
    FindRoot(p,2,1,0,1e-7)
#    print("after myroot()")

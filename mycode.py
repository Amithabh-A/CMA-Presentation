from Polynomial import Polynomial
from Polynomial import BestFitPolyFunction
import cmath

def FirstOrderDividedDifference(x0, x1, f):
    print(x1-x0)
    return (f(x1) - f(x0)) / (x1 - x0)

def SecondOrderDividedDifference(x0, x1, x2 ,f):
    return (FirstOrderDividedDifference(x1,x2,f) - FirstOrderDividedDifference(x0,x1,f)) / (x2-x0)

def FindRoot(p, x0,x1,x2,ε):
#    print("inside findroot")
    print(abs(p(x2)), ε )
    j  = 0
    while(abs(p(x2)) > ε):
        j += 1
        if(j > 10) : break
#        print("inside while loop")
        next_x = NextPoint(x0,x1,x2,p)
        print(next_x)
        i = 4
        Show(i, next_x, p)
#        x0 = x1
#        x1 = x2
#        x2 = next_x
        x0 = next_x
        x1 = x0
        x2 = x1

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
    return x2 - (2 * f(x2)) / (W(x0,x1,x2,f) + cmath.sqrt(W(x0,x1,x2,f)**2 - 4 * f(x2) * SecondOrderDividedDifference(x2,x1,x0,f)))

if __name__ == "__main__":
    # testcases

    #l = [int(x) for x in input("Enter elements separated by space: ").split()]
#    p = Polynomial([-1, -4, 0, 1])
    p = Polynomial([-1, -1, -1, 1])
    print("before myroot()")
    FindRoot(p,0,1,2,1e-7)
    print("after myroot()")
#    x0 = 10
#    x1 = 9
#    x2 = 8
#    x3 = NextPoint(x0,x1,x2,p)
#    print(x3)

from Polynomial import Polynomial
import numpy as np

def bisection_method(a, b, epsilon, f):
    while (b - a) > epsilon:
        c = (a + b) / 2
        if np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return (a + b) / 2

if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial(l)
    p.show()

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    epsilon = 10**-7
    
    print(bisection_method(a, b, epsilon, p))
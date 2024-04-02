# Newton-Raphson Method :: f -> x0 -> epsilon -> ()
from Polynomial import Polynomial
import math

def f_prime(f, x):
    return derivative(f)(x)

def next_x(f, x):
    return x - f(x) / f_prime(f, x)


def newton_raphson(f, x0, epsilon):
    while abs(f(x0)) > epsilon:
        x0 = next_x(f, x0)
    return x0

if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    f = Polynomial(l)
    f.show()

    x0 = float(input("Enter x0: "))
    epsilon = 10**-7#float(input("Enter epsilon: "))

    print(newton_raphson(f, x0, epsilon))



# Newton-Raphson Method :: f -> x0 -> epsilon -> ()
from Polynomial import Polynomial
import math

class NewtonRaphson:
    def __init__(self, coefficients):
        self.f = Polynomial(coefficients)

    def f_prime(self, x):
        f = self.derivative()  
        return f(x)
    
    def derivative(self):
        """
        Function to calculate the derivative of a polynomial
        """
        newP = []
        for i,c in enumerate(self.f.list):
            if i!=0:
                newP.append(i*c)
        
        return Polynomial(newP)


    def print_iteration(self, i, x, fx):
        print(str(i) + "\t{:.4f}".format(x) + "\t{:.4f}".format(self.f(x)))
    
    def next_x(self, x):
        return x - self.f(x) / self.f_prime(x)

    def newton_raphson(self, x0, epsilon):
        errors = []  
        print("n \t xn\tf(xn)")
        print("1 \t " + str(x0) + "\t" + str(self.f(x0)))
        i = 1
        while abs(self.f(x0)) > epsilon:
            errors.append(abs(self.f(x0)))
            x0 = self.next_x(x0)
            i += 1
            self.print_iteration(i, x0, self.f(x0))
        return x0, errors  



if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    f = Polynomial(l)
    f.show()

    x0 = float(input("Enter x0: "))
    epsilon = 10**-7#float(input("Enter epsilon: "))

    nr = NewtonRaphson(l)
    result, _ = nr.newton_raphson(x0, epsilon)  
    print(result)

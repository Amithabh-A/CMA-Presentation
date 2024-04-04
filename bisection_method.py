from Polynomial import Polynomial
import numpy as np

class Bisection:
    def __init__(self, a, b, epsilon, f):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.f = f
        self.errors = []

    def bisection_method(self):
        print("n \t xn\t\tf(xn)")
        print("1 \t " + str(self.a) + "\t\t" + str(self.f(self.a)))
        i = 1
        print(self.b-self.a)
        while abs(self.b - self.a) > self.epsilon:
            print(self.b-self.a)
            c = (self.a + self.b) / 2
            if np.sign(self.f(c)) == np.sign(self.f(self.a)):
                self.a = c
            else:
                self.b = c
            self.errors.append(abs(self.f(c)))
            i += 1

        return (self.a + self.b) / 2, self.errors, i

if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial(l)
    p.show()

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    epsilon = 10**-7

    bisection = Bisection(a, b, epsilon, p)
    ans, err, it = bisection.bisection_method()
    print(ans)
    print(it)

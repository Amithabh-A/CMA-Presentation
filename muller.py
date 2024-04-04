from Polynomial import Polynomial
import cmath

class Muller:
    def __init__(self, l, x0, x1, x2):
        self.f = Polynomial(l)
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2

    def calculate_next_x(self):
        q = (self.x2 - self.x1) / (self.x1 - self.x0)
        a = q * self.f(self.x2) - q * (1 + q) * self.f(self.x1) + q**2 * self.f(self.x0)
        b = (2 * q + 1) * self.f(self.x2) - (1 + q)**2 * self.f(self.x1) + q**2 * self.f(self.x0)
        c = (1 + q) * self.f(self.x2)
        return self.x2 - (self.x2 - self.x1) * ((2 * c) / (b + cmath.sqrt(b**2 - 4 * a * c)))

    def print_iteration(self, i, x, fx):
        if x.imag == 0j:
            x = x.real
#            print(str(i) + "\t" + str(round(x, 5)) + "\t\t" + str(round(self.f(x), 5)))
        else:
#            print(str(i) + "\t{:.4f}".format(x) + "\t{:.4f}".format(self.f(x)))
            pass

    def find_root(self):
        epsilon = 10**-7
        i = 0
        print("n \t xn\t\tf(xn)")
#        print("1 \t " + str(self.x0) + "\t\t" + str(self.f(self.x0)))
#        print("2 \t " + str(self.x1) + "\t\t" + str(self.f(self.x1)))
#        print("3 \t " + str(self.x2) + "\t\t" + str(self.f(self.x2)))
        
        while abs(self.f(self.x2)) > epsilon:
            xplus = self.calculate_next_x()
            self.print_iteration(i + 4, xplus, self.f(xplus))
            self.x0, self.x1, self.x2 = self.x1, self.x2, xplus
            i += 1
        
        
        if isinstance(xplus, complex):
            conjugate = complex(xplus.real, -xplus.imag)
            if abs(self.f(conjugate)) < epsilon:
                print("and \t{:.4f}".format(conjugate) + "\t{:.4f}".format(self.f(conjugate)))
        print(str(i) + " iterations")

if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial(l)
    p.show()

    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    
    muller = Muller(l, x0, x1, x2)
    muller.find_root()

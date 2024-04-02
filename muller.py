from Polynomial import Polynomial
import cmath

def calculate_next_x(x0, x1, x2, f):
    q = (x2 - x1) / (x1 - x0) # f [x1, x2]
    a = q * f(x2) - q * (1 + q) * f(x1) + q**2 * f(x0)
    # q * (f_xn  -q  -1)
    b = (2 * q + 1) * f(x2) - (1 + q)**2 * f(x1) + q**2 * f(x0)
    c = (1 + q) * f(x2)
    return x2 - (x2 - x1) * ((2 * c) / (b + cmath.sqrt(b**2 - 4 * a * c)))

def print_iteration(i, x, fx, f):
    # i is the iteration number. 
    if x.imag == 0j:
        x = x.real
        print(str(i) + "\t" + str(round(x, 5)) + "\t\t" + str(round(f(x), 5)))
    else:
        print(str(i) + "\t{:.4f}".format(x) + "\t{:.4f}".format(f(x)))

def find_root(f, x0, x1, x2):
    epsilon = 10**-7
    i = 0
    print("n \t xn\t\tf(xn)")
    print("1 \t " + str(x0) + "\t\t" + str(f(x0)))
    print("2 \t " + str(x1) + "\t\t" + str(f(x1)))
    print("3 \t " + str(x2) + "\t\t" + str(f(x2)))
    
    while abs(f(x2)) > epsilon:
        xplus = calculate_next_x(x0, x1, x2, f)
        print_iteration(i + 4, xplus, f(xplus), f)
        x0, x1, x2 = x1, x2, xplus
        i += 1
    
    print(str(i) + " iterations")
    
    if isinstance(xplus, complex):
        conjugate = complex(xplus.real, -xplus.imag)
        if abs(f(conjugate)) < epsilon:
            print("and \t{:.4f}".format(conjugate) + "\t{:.4f}".format(f(conjugate)))

if __name__ == '__main__':
    l = [float(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial(l)
    p.show()

    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    
    find_root(p, x0, x1, x2)

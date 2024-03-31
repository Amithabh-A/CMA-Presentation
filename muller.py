from Polynomial import Polynomial
import cmath

def f(x):
#    p = Polynomial([-1, -4, 0, 1])
    p= Polynomial([-1, -1, -1, 1])
    return p(x)

def calculate_next_x(xnm2, xnm1, xn):
    q = (xn - xnm1) / (xnm1 - xnm2) # f [xnm1, xn]
    a = q * f(xn) - q * (1 + q) * f(xnm1) + q**2 * f(xnm2)
    # q * (f_xn  -q  -1)
    b = (2 * q + 1) * f(xn) - (1 + q)**2 * f(xnm1) + q**2 * f(xnm2)
    c = (1 + q) * f(xn)
    return xn - (xn - xnm1) * ((2 * c) / (b + cmath.sqrt(b**2 - 4 * a * c)))

def print_iteration(i, x, fx):
    # i is the iteration number. 
    if x.imag == 0j:
        x = x.real
        print(str(i) + "\t" + str(round(x, 5)) + "\t\t" + str(round(f(x), 5)))
    else:
        print(str(i) + "\t{:.4f}".format(x) + "\t{:.4f}".format(f(x)))

def find_root():
    xnm2 = 2
    xnm1 = 1
    xn = 0
    epsilon = 10**-7
    i = 0
    print("n \t xn\t\tf(xn)")
    print("1 \t " + str(xnm2) + "\t\t" + str(f(xnm2)))
    print("2 \t " + str(xnm1) + "\t\t" + str(f(xnm1)))
    print("3 \t " + str(xn) + "\t\t" + str(f(xn)))
    
    while abs(f(xn)) > epsilon:
        xplus = calculate_next_x(xnm2, xnm1, xn)
        print_iteration(i + 4, xplus, f(xplus))
        xnm2, xnm1, xn = xnm1, xn, xplus
        i += 1
    
    print(str(i) + " iterations")
    
    if isinstance(xplus, complex):
        conjugate = complex(xplus.real, -xplus.imag)
        if abs(f(conjugate)) < epsilon:
            print("and \t{:.4f}".format(conjugate) + "\t{:.4f}".format(f(conjugate)))

if __name__ == '__main__':
    l = [int(x) for x in input("Enter elements separated by space: ").split()]
    p = Polynomial(l)
    find_root()

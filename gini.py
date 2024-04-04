import matplotlib.pyplot as plt
from Polynomial import Polynomial
import numpy as np

def f(x):  # Replace this with your actual function definition
    return x**2 - 2

def muller_method(f, a, b, c, tol=1e-5, max_iter=100):
    iterations = []
    errors = []
    for i in range(max_iter):
        h0 = b - a
        h1 = c - b
        d0 = f(b) - f(a)
        d1 = f(c) - f(b)
        a0 = h1 * h1 * f(a) - h0 * h0 * f(c)
        a1 = h0 * d1 - h1 * d0
        a2 = f(a)
        ba = a - a0 / (a1 + a2 * np.sqrt(a1 * a1 - 4 * a0 * a2))
        ca = a - a0 / (a1 - a2 * np.sqrt(a1 * a1 - 4 * a0 * a2))
        if abs(f(ba)) < abs(f(ca)):
            a, b, c = ba, a, b
        else:
            a, b, c = ca, b, a
        iterations.append(i + 1)
        errors.append(abs(f(a)))
        if abs(f(a)) < tol:
            break
    return iterations, errors

def secant_method(f, a, b, tol=1e-5, max_iter=100):
    iterations = []
    errors = []
    for i in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        a, b = b, c
        iterations.append(i + 1)
        errors.append(abs(f(a)))
        if abs(f(a)) < tol:
            break
    return iterations, errors

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    iterations = []
    errors = []
    for i in range(max_iter):
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        iterations.append(i + 1)
        errors.append(abs(b - a))
        if abs(b - a) < tol:
            break
    return iterations, errors

# Set up the function and initial values
l = [float(x) for x in input("Enter elements separated by space: ").split()]
p = Polynomial(l)
func = p
a = 1.0 
b = 1.5
c = 2.0

# Run the methods and collect data
muller_iters, muller_errs = muller_method(func, a, b, c)
secant_iters, secant_errs = secant_method(func, a, b)
bisection_iters, bisection_errs = bisection_method(func, a, b)

# Plot the results
plt.plot(muller_iters, muller_errs, label='Muller\'s Method')
plt.plot(secant_iters, secant_errs, label='Secant Method')
plt.plot(bisection_iters, bisection_errs, label='Bisection Method')

# Label the plot
plt.xlabel('Iterations')
plt.ylabel('Error (abs(f(x)))')
plt.title('Rate of Convergence Comparison')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

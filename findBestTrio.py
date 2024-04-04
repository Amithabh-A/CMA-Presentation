from Polynomial import Polynomial
from gemini import muller_method
import random

def find_best_trio(f, a_min, a_max, b_min, b_max, c_min, c_max, tol=1e-5, max_iter=100, num_trials=100000):
    """
    Finds the best trio of initial points (a, b, c) for Muller's method within a specified range.

    Args:
        f: The function to find the root of.
        a_min, a_max: Minimum and maximum values for the 'a' initial point.
        b_min, b_max: Minimum and maximum values for the 'b' initial point.
        c_min, c_max: Minimum and maximum values for the 'c' initial point.
        tol: Tolerance for convergence (default: 1e-5).
        max_iter: Maximum number of iterations allowed (default: 100).
        num_trials: Number of random trials to perform (default: 1000).

    Returns:
        A tuple containing the best trio (a, b, c) and the corresponding number of iterations.
    """

    best_trio = None
    best_iters = float('inf')

    for _ in range(num_trials):
        a = random.uniform(a_min, a_max)
        b = random.uniform(b_min, b_max)
        c = random.uniform(c_min, c_max)

        iters, _ = muller_method(f, a, b, c, tol, max_iter)
        if len(iters) < best_iters:
            best_trio = (a, b, c)
            best_iters = len(iters)

    return best_trio, best_iters

# Example usage (assuming your muller_method function is defined)
print("example usage")
l = [float(x) for x in input("Enter elements separated by space: ").split()]
f = Polynomial(l)
func = f  # Replace with your function

# Set the ranges for initial points (adjust as needed)
# a_min, a_max = 1.0, 1.5
# b_min, b_max = 1.1, 1.6
# c_min, c_max = 1.2, 1.7

a_min = b_min = c_min = -4
a_max = b_max = c_max = 4

best_trio, best_iters = find_best_trio(func, a_min, a_max, b_min, b_max, c_min, c_max)

print("Best trio:", best_trio)
print("Minimum iterations:", best_iters)

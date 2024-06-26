from Vector import RowVectorFloat
import matplotlib.pyplot as plt
import numpy as np

class Polynomial(RowVectorFloat):

    # powerDict = {0:'⁰', 1:'¹', 2:'²', 3:'³', 4:'⁴', 5:'⁵', 6:'⁶', 7:'⁷', 8:'⁸', 9:'⁹'}  ## Just an attempt to show powers well

    def __init__(self, l):
        """
        Construct a polynomial using a list of coefficients as input
        """
        self.list = l
        self.degree = len(self.list)      
        
        ## Take care of trailing zeroes
        self.truncate()

    def __str__(self):
        """
        Return the coefficients in printable format
        """
        return "Coefficients of the polynomial are:\n" + super().__str__()

    def __repr__(self):
        """
        Shell representation
        """
        return self.__str__()


    def __add__(self, other):
        """
        Add 2 polynomials
        """
        # Adjust degree accordingly so that polynomials of different degress can be added
        if self.degree > other.degree:
            other.list += [0]*(self.degree - other.degree)
            other.degree = self.degree
        if self.degree < other.degree:
            self.list += [0]*(other.degree - self.degree)
            self.degree = other.degree

        # call super class method
        return Polynomial(super().__add__(other).list)

    def __sub__(self, other):
        """
        Subtract 2 polynomials
        """
        return self + (-1)*other

    def __mul__(self, other):
        """
        Multiply 2 polynomials, or a polynomial and a constant
        """
        if isinstance(other, Polynomial):
            newP = [0] * (self.degree + other.degree)
            # Go through each term of each polynomial and multiply them. Put them in the correct degree.
            for i,val1 in enumerate(self.list):
                for j,val2 in enumerate(other.list):
                    newP[i+j] += val1*val2

            return Polynomial(newP)
                
        
        return Polynomial(super().__mul__(other).list)

    def __rmul__(self, other):
        return self*other

    def __getitem__(self, value):
        """
        Evaluate polynomial
        """
        powerSeries = [value**i for i in range(self.degree)]

        return sum([x_p*c for (x_p,c) in zip(powerSeries, self.list)])

    def __call__(self, value):
        return self[value]

    def __pow__(self, n):
        prod = self
        for i in range(n-1):
            prod *= self
        
        return prod

    def copy(self):
        
        return Polynomial(self.list)

    def truncate(self):
        """
        Remove trailng 0 coefficients
        """
        if len(self.list) <= 1:
            return
        while self.list[-1] == 0 and len(self.list) > 1:
            self.list.pop(-1)
        self.degree = len(self.list)

    def asString(self):
        """
        The algebraic representation of the polynomial
        """
        s = ""
        for i,c in enumerate(self.list):
            if c>=0:
                if i!=0:
                    s+="+"
                s += str(c)
            else:
                if i!=0:
                    s+="-"
                s += str(-c)
            s += "(x^" + str(i) + ")"
        return s

    def show(self, a = -10, b = 10, filename="plot.jpg"):
        """
        Plot the polynomial in the given interval and save it as a jpg file
        """    
        numpts = 100

        X = np.linspace(a,b, numpts)

        Y = [self[x] for x in X]

        plt.plot(X,Y)
        plt.title("Plot of Polynomial " + self.asString())
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.grid()
        plt.savefig(filename)
        open_jpg(filename)

    def fitViaMatrixMethod(self, l, showPlot = True):
        """
        Find a polynomial that fits the given list of points using matrix inverse
        """
        input_x = np.array([x for x,y in l])

        # Generate the matrix that represents the polynomials for each x
        A = np.array([1]*len(l))
        for i in range(len(l)-1):
            A = np.c_[A, input_x**(i+1)]
    
        b = np.array([y for x,y in l])

        ## Ax = b
        ## Solve x = A_inv*b
        try:
            X = np.linalg.inv(A) @ b
        except:
            raise Exception("Equation unsolvable")
        self = Polynomial(list(X))

        ## Plot
        if showPlot:
            numpts = 100

            X = np.linspace(min(input_x),max(input_x), numpts)

            Y = [self[x] for x in X]

            plt.plot(X,Y)
            plt.scatter(input_x, b, c='r')
            plt.title("Polynomial interpolation using matrix method")
            plt.xlabel("x")
            plt.ylabel("P(x)")
            plt.grid()
            plt.show()

        return self

    def fitViaLagrangePoly(self, l):
        """
        Find a polynomial that fits the given list of points using lagrange polynomials
        """
        n = len(l)
        X = [x for x,y in l]
        Y = [y for x,y in l]

        def psi(j):
            """
            Function to calculate the lagrange polynomial for jth x
            """
            pi = 1
            for i in range(n):
                if i!= j:
                    pi *= Polynomial([-X[i], 1])/(X[j] - X[i])
            return pi

        P = Polynomial([])
        ## calculate sum of all lagrange polynomials
        for i in range(n):
            P += Y[i]*psi(i)

        self = P

        ## Plot
        numpts = 100

        Xg = np.linspace(min(X),max(X), numpts)

        Yg = [self[x] for x in Xg]

        plt.plot(Xg,Yg)
        plt.scatter(X, Y, c='r')
        plt.title("Interpolation using Lagrange polynomial")
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.grid()
        plt.show()

        return P


    def derivative(poly, n=1):
        """
        Function to calculate the derivative of a polynomial
        """
        newP = []
        for i,c in enumerate(poly.list):
            if i!=0:
                newP.append(i*c)
        
        if n==1:
            return Polynomial(newP)
        return Polynomial(newP).derivative(n-1)

    def area(poly, a, b):
        """
        Function to calculate the definite integral of a polynomial in the given range.
        """
        newP = [0]
        for i,c in enumerate(poly.list):
            newP.append(c/(i+1))

        newP = Polynomial(newP)
        return newP[b] - newP[a]


def BestFitPoly(n, x, y, plot=False):
    X = np.zeros((len(x), n+1))
    y = np.array(y)

    # Generate a matrix with x**i as each column
    for i in range(n+1):
        X[:,i] = np.array(x)**i

    # Use linsolve to solve the system of linear equations for the coefficients.
    coeffs = np.linalg.solve(X.T @ X, X.T @ y)

    # Construct a polynomial with the coefficients
    p = Polynomial(list(coeffs))

    X_plot = np.linspace(min(x),max(x), 100)
    Y_plot = [p[i] for i in X_plot]

    if plot:
        plt.title("Best fit polynomial of degree " + str(n) + " on given points")
        plt.scatter(x, y, c="r")
        plt.plot(X_plot, Y_plot)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()

    return p

def BestFitPolyFunction(n, f, a=0, b=1, M=1000, f_name = "", plot=False):
    ## Applies BestFitPoly on a function, simply takes many points of the function and runs BestFitPoly on thsoe points
    X = np.linspace(a, b, M)

    pts = [f(x) for x in X]

    p = BestFitPoly(n, X, pts, plot=False)

    if plot:
        X = np.linspace(a, b, M)
        Y_f = np.vectorize(f)(X)
        Y_p = [p[x] for x in X]
        plt.title("Best fit polynomial of degree "+ str(n) + " to given function " + f_name)
        plt.plot(X, Y_f, label=f_name if f_name != "" else "f(x)")
        plt.plot(X, Y_p, label="P(x)")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    return p


def aberth_method(P : Polynomial, ɛ, Z):
    n = P.degree-1

    if n==0:
        return None

    Z0 = [z+10*ɛ for z in Z]


    while any([abs(Z[i] - Z0[i])>ɛ for i in range(n)]):
        memo = [sum([1/(Z[k] - Z[j])  if j!=k else 0 for j in range(n)]) for k in range(n)]
        Z0 = Z.copy()
        for i in range(n): 
            t = P(Z[i])/P.derivative()(Z[i])
            Z[i] -= t/(1 - t*memo[i])

    return Z

def open_jpg(file_path):
    from PIL import Image
    try:
        with Image.open(file_path) as img:
            img.show()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

Polynomial.printRoots = lambda self,Z0: aberth_method(self, 10e-3, Z0)

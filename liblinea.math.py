class Basic:
    def sqrt(self, x):
        return x ** 0.5
    
    def square(self, x):
        return x ** 2
    
    def cube(self, x):
        return x ** 3
    
    def power(self, x, y):
        return x ** y
    
    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)
        
    def fact(self, x):
        return self.factorial(x)
    
    def abs(self, x):
        return abs(x)
    
class Trig:
    def sin(self, x):
        import math
        return math.sin(x)
    
    def cos(self, x):
        import math
        return math.cos(x)
    
    def tan(self, x):
        import math
        return math.tan(x)
    
    def asin(self, x):
        import math
        return math.asin(x)
    
    def acos(self, x):
        import math
        return math.acos(x)
    
    def atan(self, x):
        import math
        return math.atan(x)
    
    def sinh(self, x):
        import math
        return math.sinh(x)
    
    def cosh(self, x):
        import math
        return math.cosh(x)
    
    def tanh(self, x):
        import math
        return math.tanh(x)
    
    def asinh(self, x):
        import math
        return math.asinh(x)
    
    def acosh(self, x):
        import math
        return math.acosh(x)
    
    def atanh(self, x):
        import math
        return math.atanh(x)
    
    def sec(self, x):
        import math
        return 1 / math.cos(x)
    
    def cosec(self, x):
        import math
        return 1 / math.sin(x)
    
    def cot(self, x):
        import math
        return 1 / math.tan(x)
    
    def secant(self, x):
        import math
        return 1 / math.cos(x)
    
class Logarithm:
    def log(self, x, base=10):
        import math
        return math.log(x, base)
    
    def ln(self, x):
        import math
        return math.log(x)
    
    def log2(self, x):
        import math
        return math.log2(x)
    
    def log10(self, x):
        import math
        return math.log10(x)
    
    def logn(self, x, n):
        import math
        return math.log(x, n)
    
    def logb(self, x, b):
        import math
        return math.log(x, b)
    
class Statistics:
    def mean(self, data):
        return sum(data) / len(data)
    
    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]
    
    def mode(self, data):
        from collections import Counter
        data_count = Counter(data)
        max_count = max(data_count.values())
        modes = [k for k, v in data_count.items() if v == max_count]
        return modes[0] if len(modes) == 1 else modes
    
    def stddev(self, data):
        mean = self.mean(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance ** 0.5
    
    def variance(self, data):
        mean = self.mean(data)
        return sum((x - mean) ** 2 for x in data) / len(data)
    
    def stdev(self, data):
        return self.stddev(data)
    
class Matrix:
    def add(self, A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    def subtract(self, A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    def multiply(self, A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    
    def transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    def determinant(self, A):
        if len(A) == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        else:
            det = 0
            for c in range(len(A)):
                det += ((-1) ** c) * A[0][c] * self.determinant([row[:c] + row[c+1:] for row in A[1:]])
            return det
    
    def inverse(self, A):
        from numpy.linalg import inv
        import numpy as np
        return inv(np.array(A)).tolist()
    
    def rank(self, A):
        import numpy as np
        return np.linalg.matrix_rank(np.array(A))
    
    def eigenvalues(self, A):
        import numpy as np
        return np.linalg.eigvals(np.array(A))
    
    def eigenvectors(self, A):
        import numpy as np
        return np.linalg.eig(np.array(A))[1].tolist()
    
    def eigen(self, A):
        import numpy as np
        return np.linalg.eig(np.array(A))
    
    def eigenvalue(self, A):
        import numpy as np
        return np.linalg.eigvals(np.array(A))
    
    def eigenvector(self, A):
        import numpy as np
        return np.linalg.eig(np.array(A))[1].tolist()
    
class Complex:
    def complex(self, a, b):
        return complex(a, b)
    
    def real(self, z):
        return z.real
    
    def imag(self, z):
        return z.imag
    
    def abs(self, z):
        return abs(z)
    
    def arg(self, z):
        import cmath
        return cmath.phase(z)
    
    def polar(self, z):
        import cmath
        return cmath.polar(z)
    
    def rect(self, r, phi):
        import cmath
        return cmath.rect(r, phi)
    
    def conjugate(self, z):
        return z.conjugate()
    
    def polar(self, z):
        import cmath
        return cmath.polar(z)
    
    def rect(self, r, phi):
        import cmath
        return cmath.rect(r, phi)
    
class Calculus:
    def derivative(self, f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)
    
    def integral(self, f, a, b, n=1000):
        h = (b - a) / n
        return sum(f(a + i * h) for i in range(n)) * h
    
    def limit(self, f, x):
        import sympy as sp
        x = sp.symbols('x')
        return sp.limit(f(x), x, x)
    
    def diff(self, f, x):
        import sympy as sp
        x = sp.symbols('x')
        return sp.diff(f(x), x)
    
    def integrate(self, f, x):
        import sympy as sp
        x = sp.symbols('x')
        return sp.integrate(f(x), x)
    
class Geometry:
    def area_circle(self, r):
        return 3.14159 * r ** 2
    
    def circumference_circle(self, r):
        return 2 * 3.14159 * r
    
    def area_rectangle(self, l, w):
        return l * w
    
    def perimeter_rectangle(self, l, w):
        return 2 * (l + w)
    
    def area_triangle(self, b, h):
        return 0.5 * b * h
    
    def perimeter_triangle(self, a, b, c):
        return a + b + c
    
    def area_square(self, s):
        return s ** 2
    
    def perimeter_square(self, s):
        return 4 * s
    
    def volume_cube(self, s):
        return s ** 3
    
    def surface_area_cube(self, s):
        return 6 * s ** 2
    
    def volume_sphere(self, r):
        return (4 / 3) * 3.14159 * r ** 3
    
    def surface_area_sphere(self, r):
        return 4 * 3.14159 * r ** 2
    
    def volume_cylinder(self, r, h):
        return 3.14159 * r ** 2 * h
    
    def surface_area_cylinder(self, r, h):
        return 2 * 3.14159 * r * (r + h)
    
    def volume_cone(self, r, h):
        return (1 / 3) * 3.14159 * r ** 2 * h
    
    def surface_area_cone(self, r, h):
        return 3.14159 * r * (r + (h ** 2 + r ** 2) ** 0.5)
    
    def volume_prism(self, b, h):
        return b * h
    
    def surface_area_prism(self, b, h):
        return 2 * b + 3 * h
    
    def volume_pyramid(self, b, h):
        return (1 / 3) * b * h
    
    def surface_area_pyramid(self, b, h):
        return b + (b ** 2 + h ** 2) ** 0.5 * b
    
    def area_trapezoid(self, a, b, h):
        return 0.5 * (a + b) * h
    
    def perimeter_trapezoid(self, a, b, c, d):
        return a + b + c + d
    
class Probability:
    def probability(self, a, b):
        return a / b
    
    def combination(self, n, r):
        from math import factorial
        return factorial(n) / (factorial(r) * factorial(n - r))
    
    def permutation(self, n, r):
        from math import factorial
        return factorial(n) / factorial(n - r)
    
    def binomial(self, n, p):
        from math import comb
        return comb(n, p) * (p ** n) * ((1 - p) ** (n - p))
    
    def poisson(self, x, lam):
        from math import exp
        return (lam ** x * exp(-lam)) / Basic.factorial(x)
    
    def normal(self, x, mu, sigma):
        from math import exp, sqrt, pi
        return (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    def uniform(self, a, b):
        return 1 / (b - a)
    
    def exponential(self, x, lam):
        from math import exp
        return lam * exp(-lam * x)
    
    def geometric(self, p, x):
        return p * ((1 - p) ** (x - 1))
    
class Financial:
    def future_value(self, p, r, n):
        return p * (1 + r) ** n
    
    def present_value(self, f, r, n):
        return f / (1 + r) ** n
    
    def annuity(self, pmt, r, n):
        return pmt * ((1 - (1 + r) ** -n) / r)
    
    def loan_payment(self, p, r, n):
        return (p * r) / (1 - (1 + r) ** -n)
    
    def interest_rate(self, pmt, pv, n):
        return ((pmt / pv) ** (1 / n)) - 1
    
    def net_present_value(self, cash_flows, rate):
        npv = 0
        for t in range(len(cash_flows)):
            npv += cash_flows[t] / (1 + rate) ** t
        return npv
    

    def internal_rate_of_return(self, cash_flows):
        from scipy.optimize import newton
        npv = lambda r: sum(cf / (1 + r) ** t for t, cf in enumerate(cash_flows))
        return newton(npv, 0.1)
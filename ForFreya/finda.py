# first of, how to calculate C and S

from functools import reduce
from typing import Callable
from numpy import sin, cos, tan
import numpy as np

PI = 3.1415926535

def factorial(n: int) -> int:
    return reduce(lambda a, b: a*b, range(2, n+1), 1)

def S(x: float, number_of_terms: int = 10) -> float:
    return sum([
        (-1)**i * x**(4*i+3)/(factorial(2*i+1) * (4*i + 3))
        for i in range(number_of_terms)])

def C(x: float, number_of_terms: int = 10) -> float:
    return sum([
        (-1)**i * x**(4*i+1)/(factorial(2*i) * (4*i + 1))
        for i in range(number_of_terms)])

# okai, now the function
# f(a) = y - \tan(\theta) * (\delta_x - x)

def get_fxy(L: float, theta: float, delta_x: float) -> float:
    class Fxy:
        def x(self, a: float) -> float:
            return a*C(L/a) - (a**2 * sin(L**2 / a**2))/(2 * L)

        def y(self, a: float) -> float:
            return a*S(L/a) + (a**2 * cos(L**2 / a**2))/(2 * L)

        def f(self, a: float) -> float:
            return self.y(a) - tan(theta) * (delta_x - self.x(a))

    return Fxy()

def binary_search(negative_edge: float, positive_edge: float, 
    f: Callable[[float], float]) -> float:
    THRESHOLD = 1e-6
    assert(f(positive_edge) > 0)
    assert(f(negative_edge) < 0)

    l = positive_edge
    r = negative_edge
    while True:
        m = (l + r)/2
        if abs(f(m)) < THRESHOLD:
            return m
        if f(m) > 0:
            l = m
        else:
            r = m

def solve(L: float, theta: float, delta_x: float) -> float:
    fxy = get_fxy(L, theta, delta_x)
    a = binary_search(0.1, 2, fxy.f) # nasty constants
    return a





# L = 1
# theta = PI/4
# delta_x = 1
# f = get_f(L, theta, delta_x)



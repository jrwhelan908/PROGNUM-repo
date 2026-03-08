#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy.integrate import quad
import matplotlib.pyplot as plt

def user_func(x, expression):
    return eval(expression)

def monte_carlo_int(func, a, b, n=100000):
    x_random = np.random.uniform(a, b, n)
    y_random = func(x_random)
    return (b - a) * np.mean(y_random)

expression = input("Enter a function f(x): ")

a = 0
b = pi

try:
    test = user_func(1.0, expression)

    result_quad, error = quad(user_func, a, b, args=(expression,))
    print("Integral using quad =", result_quad)

    result_mc = monte_carlo_int(lambda x: user_func(x, expression), a, b)
    print("Integral using Monte Carlo =", result_mc)

except NameError:
    print("Error: Unknown function or variable used!")
    print("Use sin, cos, exp, pi and write x correctly.")

except SyntaxError:
    print("Error: Wrong mathematical expression")
    print("Example of correct format: x**4 + sin(x) + 2")


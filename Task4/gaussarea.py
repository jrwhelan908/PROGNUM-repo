#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return A * np.exp(-(x - x0)**2 / (2 * sigma**2)) + z0

A = float(input("Enter amplitude, A:"))
x0 = float(input("Enter position of peak, x0:"))
sig = float(input("Enter width of the peak, sigma:"))
z0 = float(input("Enter offset in y, z0:"))

xmin = float(input("Enter lower integration limit:"))
xmax = float(input("Enter upper integration limit:"))

area, error = quad(gauss, xmin, xmax, args=(A, x0, sig, z0))

print("Area under curve =", area)

x = np.linspace(xmin - 5, xmax + 5, 400)
y = gauss(x, A, x0, sig, z0)

plt.figure()
plt.plot(x, y, label="Gaussian")

x_fill = np.linspace(xmin, xmax, 400)
y_fill = gauss(x_fill, A, x0, sig, z0)
plt.fill_between(x_fill, y_fill, alpha=0.3, label="Area = {:.3f}".format(area))

plt.title("Gaussian Area")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.show()


# ![Screenshot 2026-03-08 at 19.05.41.png](attachment:e20bafef-ed6a-4998-aefe-9efcf0aa6564.png)

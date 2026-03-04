#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

function = input("Enter a function f(x)=")

a = float(input("Enter lower bound a ="))
b = float(input("Enter upper bound b ="))
N = int(input("Enter number of random points ="))

x = np.random.uniform(a,b,N)

f = eval(function)

integral = (b-a) * (1/N) * np.mean(f)

print(f"Result of integral: {integral:.6f}")


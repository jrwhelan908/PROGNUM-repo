#!/usr/bin/env python
# coding: utf-8

# In[5]:


from math import sqrt

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

D = b**2 - 4*a*c

if D>0:
    x1 = (-b+(sqrt(D))/(2*a))
    x2 = (-b-(sqrt(D))/(2*a))
    print(f"Two solutions: x1 = {x1} and x2 = {x2}")

elif D==0:
    x = (-b/(2*a))
    print(f"One solution: x = {x}")

else:
    print("No real solutions")


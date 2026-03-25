#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
from matplotlib import pyplot as plt

x_range = list(range(-5,6))
y_range = np.cosh(x_range)

plt.figure()
plt.plot(x_range, y_range, marker='o', color='red', label="y = cosh(x) using range()") 
plt.title("A catenary representation")   
plt.xlabel("x values")
plt.ylabel("cosh of x")    
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid()                                          
plt.legend(fontsize = 10)                                        
plt.show()

x_range = np.arange(-5,6,1)
y_range = np.cosh(x_range)

plt.figure()
plt.plot(x_range, y_range, marker='o', color='red', label="y = cosh(x) using range()") 
plt.title("A catenary representation")   
plt.xlabel("x values")
plt.ylabel("cosh of x")    
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid()                                          
plt.legend(fontsize = 10)                                        
plt.show()


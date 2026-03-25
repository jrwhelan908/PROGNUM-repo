#!/usr/bin/env python
# coding: utf-8

# In[13]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

M_moon = 7.349e+22
new_masses = []

for M in masses:
    if M <= M_moon:
            new_masses.append(M)
        
print("Mass lower or equal to Moon: ", new_masses)

print("Last 5 terms of list: ", masses[6:11])

print("Sum of last 5 terms: ", sum(masses[6:11]))
print("Number of elements: ", len(masses[6:11]))


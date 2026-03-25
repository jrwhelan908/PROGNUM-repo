#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
        
    def fibo(self, N, M):
        """ Return the Fibonacci numbers less than N that can be divided by M.
        This function is written by dmeindertsma on 25-02-2026.
        Parameters: N,M
        """
# Fibonacci sequence less than N
    
        x=[0,1]
        while len(x)< N:
            x.append(x[-2]+x[-1])
        
# Numbers that can be divided by M
    
        result=[]
        for value in x:
            if value%M==0:
                result.append(value)
        return result

    def nth_term(self, N):
        """
        Return the N-th Fibonacci number (0-indexed)
        """
        x = [0, 1]
        while len(x) < N:
            x.append(x[-2] + x[-1])
        return x[-1]  # N-th term
    
fib = Fibonacci()

# N-th term
print("100th Fibonacci number:", fib.nth_term(N=100))

# Fibonacci numbers < N-th term divisible by 7
print("Fibonacci numbers divisible by 7:", fib.fibo(N=100, M=7))


# In[ ]:





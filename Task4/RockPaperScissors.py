#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# First user inputs R for rock, P for paper, S for scissors

user = input("User choice (R, P, S): ").upper()

# Then the computer will answer R, P, or S at random in response

options = np.array(['R', 'P', 'S'])                 # Computer can choose between R for rock, P for paper, and S for scissors
indx = np.random.randint(0, len(options))           # Answers 1 of the 3 options per game
computer = options[indx]                            # Computer's output

print("Computer choice:", computer)                 # Computer will print R or P or S at random

# Judge the result: who wins, who loses, and if there is a tie

if user == computer:
    print("Tie")
    
elif (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
    print("User wins")

else:
    print("Computer wins")


# In[ ]:





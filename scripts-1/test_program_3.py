"""
Filename: scripts-1/test_program_3.py
Authors: Caique Miranda
"""

from random import normalvariate
import matplotlib.pyplot as plt

def generate_data(n):
    epsilon_values = []
    for i in range(n):
        e = normalvariate(0, 1)
        epsilon_values.append(e)
    
    return epsilon_values

data = generate_data(100)
plt.plot()
"""
Filename: scripts-1/test_program_2.py
Authors: Caique Miranda
"""

from random import normalvariate
import matplotlib.pyplot as plt

ts_length = 100
epsilon_values = []
i = 0
while i < ts_length:
    e = normalvariate(0, 1)
    epsilon_values.append(e)
    i = i + 1

plt.plot(epsilon_values, 'b-')
plt.show()
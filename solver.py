import numpy as np
import datetime as datetime
import pandas as pd
#import matplotlib.pyplot as plt
from pulp import LpProblem, LpVariable, LpMinimize, value, PULP_CBC_CMD

# Define some parameter Values
p = [0.5 if i < 14 or i >= 44 else 1.9 for i in range(48)]
d= 


# Define the problem
prob = LpProblem("MyProblem", LpMinimize)

# Define variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Define objective function
prob += 2 * x + 3 * y

# Define constraints
prob += x + y <= 10
prob += x - y >= 3

# Solve the problem using the default CBC solver
prob.solve(PULP_CBC_CMD())

# Print the results
print(f"Status: {prob.status}")
print(f"x = {value(x)}")
print(f"y = {value(y)}")
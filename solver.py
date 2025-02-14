import numpy as np
import datetime as datetime
import pandas as pd
#import matplotlib.pyplot as plt
from pulp import LpProblem, LpVariable, LpMinimize, value, PULP_CBC_CMD, lpSum

# Define the problem

def model_home(p, d, e):
    # Define the problem
    prob = LpProblem("MyProblem", LpMinimize)

    # Define variables
    x = [LpVariable(f"x_{i}", lowBound=0) for i in range(len(d))]
    y = [LpVariable(f"y_{i}", lowBound=0) for i in range(len(d))]  # Auxiliary variables

    # Define objective function
    prob += lpSum((p[i] * x[i]) + y[i] * e[i]  for i in range(len(d)))

    # Define constraints
    for i in range(len(d)):
        prob += y[i] >= d[i] - x[i]
        prob += y[i] >= 0

    # Solve
    prob.solve(PULP_CBC_CMD())

    # Print the results
    for i in range(len(x)):
        print(f"x_{i} = {value(x[i])}")
        
    print(f"Status: {prob.status}")

    return [value(x[i]) for i in range(len(x))]

    
import numpy as np
from optimize import minimizeFunc

def eqn(params, args):
    a,b,c,d,e,f=params
    x,y=args
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

args=(1, 2)

initial_guess=[0,0,0,0,0,0]

optimized_constants=minimizeFunc(eqn, initial_guess, args)

print("Optimized constants: ", optimized_constants)
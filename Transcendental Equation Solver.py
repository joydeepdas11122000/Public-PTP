import numpy as np
import scipy.optimize as spo

def f(x):
    return x-np.sin(x)*np.cos(x)-0.3*np.pi #Enter the Function Here

root = spo.fsolve(f, 1)[0]  #Provide a initial Guess Here after ","

print("x =",root)

# *(180/np.pi)
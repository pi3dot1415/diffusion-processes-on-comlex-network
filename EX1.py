#TODO:
# - check the formula for R0 numerically 
#       (with fixed N and different beta and r)
#       check both to have R0>1
# - 


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model_SIR (S:int, I:int, R:int, beta:float, r:float, T:float):
    '''
    Arguments:
        beta (float): parameter for infectivity
        r (float): recovery rate (constant per capita)
    '''
    y0 = (S, I, R)
    t=np.linspace(0, T, T*365+1)
    sol = odeint (ode_SIR, y0, t, args=(beta, r))
    print(sol[-1,1])
    plt.plot(t, sol[:,0], "g", label="susceptible")
    plt.plot(t, sol[:,1], "r", label="infected")
    plt.plot(t, sol[:,2], "b", label="recovered")
    plt.legend()
    plt.grid(True)
    plt.show()


def ode_SIR(y,t,beta,r):
    S, I, R = y
    dydt = [-beta*S*I, beta*S*I-r*I, r*I]
    return dydt

S=100
I=1
R=0
beta=0.008
r=0.8
T=2000

print(f"R_0 = {beta*(S+I+R)/r}")

model_SIR(S, I, R, beta, r, T)

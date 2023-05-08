import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


def step(x:float, y:float, x_lmt:float, y_lmt:float)->tuple:
    """
    Function calculate new coordinates of agent after single step.
    
    Arguments:
        x (float): initial x-axis coordinate (should be from [-x_lmt,x_lmt]).
        y (float): initial y-axis coordinate (should be from [-y_lmt,y_lmt]).
        x_lmt (float): limit on x-axis (x can move in [-x_lmt,x_lmt].
        y_lmt (float): limit on y-axis (y can move in [-y_lmt,y_lmt].
        
    Returns:
        (x,y) (tuple): new agent coordinates.
    """
    
    #Create random angel
    randVar=np.random.random()*2*np.pi
    
    #As long as agent go out of plane choosing new coordinates
    while (abs(x+np.sin(randVar))>x_lmt) or (abs(y+np.cos(randVar))>y_lmt):
        randVar=np.random.random()*2*np.pi
    
    #Updating coordinates
    x+=np.sin(randVar)
    y+=np.cos(randVar)
    
    #Return new coordinates
    return(x,y)

def random_Pearson_walk (x0:float=0, y0:float=0, x_lmt:float=20, y_lmt:float=20, steps:int=1000)->tuple:
    """
    Function creates simulation of Pearson random walk for given initial coordinates, 
    x- and y-axis coordinations, and number of steps.
    
    Arguments:
        x_0 (float): initial x-axis coordinate (should be from [-x_lmt,x_lmt]), deafult 0.
        y_0 (float): initial y-axis coordinate (should be from [-y_lmt,y_lmt]), deafult 0.
        x_lmt (float): limit on x-axis (x can move in [-x_lmt,x_lmt], deafult 20.
        y_lmt (float): limit on y-axis (y can move in [-y_lmt,y_lmt], deafult 20.
        steps (int): number of steps in simulation, deafult 1000.
        
    Returns:
        result (tuple): percent of hitting right half-plane or first quater respectively.
    """
    
    #Setting x0 and y0 as x and y respectively.
    x, y = x0, y0
    
    #Setting A and B counters to 0
    countA = 0
    countB = 0

    #Running one simulation, and for every step checking if agent exist in right half-plane or first quater
    for i in range(steps):
        (x,y)=step(x,y,x_lmt,y_lmt)
        if x>0:
            countA+=1
            if y>0:
                countB+=1
    #Return percent of hitting right half-plane or first quater respectively. 
    return(countA/steps, countB/steps)

#Setting number of simulations to 1000 as N
N=1000

#Creating lists for storing results for A and B
A=[]
B=[]

#Running all simulations N-times
for i in range(N):
    (a,b)=random_Pearson_walk()
    A.append(a)
    B.append(b)

#Plotting histograms of distribution A and B
plt.subplot(1,2,1)
plt.hist(A, bins=50, density=True)
plt.title("probability distribution of A")
plt.xlabel("fraction of occurance in right-half plane")
plt.ylabel("density")
plt.grid("True")
plt.subplot(1,2,2)
plt.hist(B, bins=50, density=True)
plt.title("probability distribution of B")
plt.xlabel("fraction of occurance in first quadrant of plane")
plt.ylabel("density")
plt.grid("True")
plt.show()


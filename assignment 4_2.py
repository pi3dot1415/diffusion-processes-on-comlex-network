import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


def step(x:float, y:float, x_lmt:float, y_lmt:float)->tuple:
    """
    """
    randVar=np.random.random()*2*np.pi
    while (abs(x+np.sin(randVar))>x_lmt) or (abs(y+np.cos(randVar))>y_lmt):
        randVar=np.random.random()*2*np.pi
    x+=np.sin(randVar)
    y+=np.cos(randVar)

    return(x,y)

def random_Pearson_walk (x0:float=0, y0:float=0, x_lmt:float=20, y_lmt:float=20, steps:int=1000)->tuple:
    """
    """
    x, y = x0, y0
    countA = 0
    countB = 0

    for i in range(steps):
        (x,y)=step(x,y,x_lmt,y_lmt)
        if x>0:
            countA+=1
            if y>0:
                countB+=1

    return(countA/steps, countB/steps)

N=1000
A=[]
B=[]

for i in range(N):
    (a,b)=random_Pearson_walk()
    A.append(a)
    B.append(b)

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


#!/usr/bin/env python
# coding: utf-8

# ## TODO:
# - Finish point b) of excersise 1
# - Finish excersise 2
# - Made excersise 3
# - And, of course, coments and documentation

# ### Excersise 1

# In[1]:


#Importing packages
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# #### Standard SIR model

# Creating functions

# In[2]:


def model_SIR (S:int, I:int, R:int, beta:float, r:float, T:float) -> None:
    '''
    Function generates plot (based on SIR model) which show number of infected, suspectible
    and removed in time for given parameters.
    
    Arguments:
        S (int): Number of suspectible
        I (int): Number of infected
        R (int): Number of removed
        beta (float): parameter for infectivity
        r (float): recovery rate (constant per capita)
        T (float): Time of simulation (there is 365*T+1 steps in simulation)
    
    Return:
        None
    '''
    #initial conditions
    y0 = (S, I, R)
    #vector of t in [0,T]
    t=np.linspace(0, T, T*365+1)
    #numerically solved ode
    sol = odeint (ode_SIR, y0, t, args=(beta, r))
    #plot of S(t), I(t), R(t)
    plt.plot(t, sol[:,0], "g", label="susceptible")
    plt.plot(t, sol[:,1], "r", label="infected")
    plt.plot(t, sol[:,2], "b", label="recovered")
    plt.title(f"model SIR for $\\beta$={beta} & $r$={r}")
    plt.xlabel("Time")
    plt.ylabel("Amount of people")
    plt.legend()
    plt.grid(True)
    plt.show()


# In[3]:


def ode_SIR(y:tuple, t:np.ndarray, beta:float, r:float):
    """
    Function solves SIR models ODE.
    
    Arguments:
        y (tuple): initial condition for S, I & R
        t (np.ndarray); array of times
        beta (beta): parameter for infectivity
        r (float): recovery rate
    Return:
        dydt (list): solution for ODE
    """
    S, I, R = y
    #specify equations
    dydt = [-beta*S*I, beta*S*I-r*I, r*I]
    return dydt


# Setting parameters

# In[4]:


S=1000
I=10
R=0
T=50

beta1=0.0008
r1=0.9

beta2=0.0008
r2=0.5

beta3=0.0012
r3=0.9

beta4=0.0012
r4=0.5

beta5=0.002
r5=0.5


# Running simulations for different parameters

# In[5]:


print(f"R0_1 = {beta1*(S+I+R)/r1}")
model_SIR(S, I, R, beta1, r1, T)


# In[6]:


print(f"R0_2 = {beta2*(S+I+R)/r2}")
model_SIR(S, I, R, beta2, r2, T)


# In[7]:


print(f"R0_3 = {beta3*(S+I+R)/r3}")
model_SIR(S, I, R, beta3, r3, T)


# In[8]:


print(f"R0_4 = {beta4*(S+I+R)/r4}")
model_SIR(S, I, R, beta4, r4, T)


# In[9]:


print(f"R0_5 = {beta5*(S+I+R)/r5}")
model_SIR(S, I, R, beta5, r5, T)


# #### Reduced SIr model

# Creating functions

# In[10]:


def model_SI (S:int, I:int, beta:float, r:float, T:float) -> None:
    '''
    Function generates quiver plo (based on SI model) 
    which show number of infected, suspectibe in time for given parameters.
    
    Arguments:
        S (int): Number of suspectible
        I (int): Number of infected
        beta (float): parameter for infectivity
        r (float): recovery rate (constant per capita)
        T (float): Time of simulation (there is 365*T+1 steps in simulation)
    
    Return:
        None
    '''
    
    #initial conditions
    y0 = (S, I)
    
    #vector of t in [0,T]
    t=np.linspace(0, T, T*365+1)
    
    y1 = np.arange(.0004, .0020, .0001)
    y2 = np.arange(.1, .9, .05)

    beta, r = np.meshgrid(y1, y2)

    u, v = np.zeros(beta.shape), np.zeros(r.shape)

    NI, NJ = beta.shape

    for i in range(NI):
        for j in range(NJ):
            x = beta[i, j]
            y = r[i, j]
            yprime = odeint(ode_SI, y0, t, args=(x,y))[-1]
            u[i,j] = yprime[0]
            v[i,j] = yprime[1]
        
    fig, ax = plt.subplots()
    q = ax.quiver(y1,y2,u,v)
    ax.set_xlabel("$\\beta$")
    ax.set_ylabel("r")
    plt.show()


# In[41]:


def ode_SI(y:tuple, t:np.ndarray, beta:float, r:float):
    """
    Function solves SI models ODE.
    
    Arguments:
        y (tuple): initial condition for S, I & R
        t (np.ndarray); array of times
        beta (beta): parameter for infectivity
        r (float): recovery rate
    Return:
        dydt (list): solution for ODE
    """
    S, I = y
    #specify equations
    dydt = [-beta*S*I, beta*S*I-r*I]
    return dydt


# Try to solve this excercice

# In[48]:


beta,r = np.meshgrid(np.arange(.0004, .0020, .0001), np.arange(.1, .9, .05))
z = beta*np.exp(-beta**2 - r**2)
v, u = np.gradient(z, .2, .2)
fig, ax = plt.subplots()
q = ax.quiver(beta,r,u,v)
ax.set_xlabel("$\\beta$")
ax.set_ylabel("r")
plt.show()


# In[51]:


y1 = np.arange(0, T, 1)
y2 = np.arange(0, )

beta, r = np.meshgrid(y1, y2)
v, u = np.gradient(z, .2, .2)

def f(Y, t):
    y1, y2 = Y
    return [y2, 100*np.cos(y1)]

t = 10

u, v = np.zeros(beta.shape), np.zeros(r.shape)


NI, NJ = beta.shape

for i in range(NI):
    for j in range(NJ):
        x = u[i, j]
        y = v[i, j]
        yprime = ode_SI([y1, y2], t, beta, r)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
        
fig, ax = plt.subplots()
q = ax.quiver(y1,y2,u,v)
ax.set_xlabel("$\\beta$")
ax.set_ylabel("r")
plt.show()


# In[50]:


yS = np.arange(0, S+I, 40)
yI = np.arange(0, S+I, 40)

x, y = np.meshgrid(yS, yI)

u=x
v=y

fig, ax = plt.subplots()
q = ax.quiver(yS,yI,u,v)
ax.set_xlabel("$\\beta$")
ax.set_ylabel("r")
plt.show()


# #### Total number of infected

# In[52]:


def total_of_SI (S:int, I:int, beta:float, r:float, T:float) -> None:
    '''
    Function generates plot (based on SI model) 
    which show total number of infected.
    Also we assume that initial value of R = 0
    
    Arguments:
        S (int): Number of suspectible
        I (int): Number of infected
        beta (float): parameter for infectivity
        r (float): recovery rate (constant per capita)
        T (float): Time of simulation (there is 365*T+1 steps in simulation)
    
    Return:
        None
    '''
    #total number of people considered in model
    N=S+I
    #initial conditions
    y0 = (S, I)
    #vector of t in [0,T]
    t=np.linspace(0, T, T*365+1)
    #numerically solved ode
    sol = odeint (ode_SI, y0, t, args=(beta, r))
    #calculate total infected
    ttl_inf = []
    ttl = np.linspace(N,N,len(sol[:,0]))
    for s in sol[:,0]:
        ttl_inf.append(N-s)
    #printing R0 and number of total infected
    print(f"R0={beta*(S+I)/r}, total number of infected = {ttl_inf[-1]}")
    #plot of total infected
    plt.plot(t, ttl_inf, "r", label="total n. of infected")
    plt.plot(t, ttl, "b", label="N")
    plt.title(f"model SI for $\\beta$={beta} & $r$={r}")
    plt.xlabel("Time")
    plt.ylabel("Number of infected")
    plt.legend()
    plt.grid(True)
    plt.show()


# In[53]:


total_of_SI(S, I, beta1, r1, T)


# In[54]:


total_of_SI(S, I, beta2, r2, T)


# In[55]:


total_of_SI(S, I, beta3, r3, T)


# In[56]:


total_of_SI(S, I, beta4, r4, T)


# In[57]:


total_of_SI(S, I, beta5, r3, T)


# ### Excersise 2

# importing libraries

# In[102]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# creating definitions

# In[239]:


def model_SIR_on_graph (G:nx.Graph, I:any, p:float) -> tuple:
    """
    Function create simulation of SIR model on graph.
    The simulation runs untill there is zero infected nodes
    
    Arguments:
        G (nx.Graph): graph on which simulation will be run
        I (int|float|str): infected node
        p (float): probability of spreading virus
    
    Return:
        Num_inf (list): history of number of infected nodes during time
        total_inf (int): number of all nodes which were infected during simulation
        iterator (int): time of pandemic
        max_inf_time (int): time when were the most infected people
    """
    #Creating lists for all possible cases for nodes
    nodes = G.nodes()
    Susceptible = []
    for nds in nodes:
        Susceptible.append(nds)
    Susceptible.remove(I)
    Infected = [I]
    Removed = []
    
    all_nodes=len(Susceptible)
    iterator = 0 
    Num_inf = [1/all_nodes]
    
    while len(Infected)>0:
        temp_inf=[]
        for inf in Infected:
            for neigh in G.neighbors(inf):
                if (neigh in Susceptible) & (neigh not in temp_inf):
                    if np.random.random()<p:
                        temp_inf.append(neigh)
                        try:
                            Susceptible.remove(neigh)
                        except:
                            pass
        Removed += Infected
        Infected = temp_inf
        iterator += 1
        Num_inf.append(len(Infected)/all_nodes)
        
    max_inf_time=Num_inf.index(max(Num_inf))
    total_inf = len(Removed)
    return(Num_inf, total_inf, iterator, max_inf_time)


# In[198]:


#Create list of probabilities and set number of iterations to 100
probs = [0.1, 0.5, 0.9]
iters = 100
t = np.arange(100)


# In[199]:


#square latice
m = 10 #overall population is equal m**2
I_latice = (np.random.randint(m), np.random.randint(m)) # randomly choosing first infected node


# In[216]:


#Loop for simulate on all of probabilities on list
for prob in probs:
    max_inf=0
    res=np.zeros(100)
    #100 times we simulate SIR model 
    for i in range (iters):
        G_latice = nx.grid_2d_graph(m,m)
        one_res = model_SIR_on_graph(G_latice, I_latice, prob)
        if one_res[2]>max_inf:
            max_inf=one_res[2]
        for i in range(len(one_res[0])):
            res[i] += one_res[0][i]/(m**2*iters)

    #Plot results
    plt.plot(t[:max_inf], res[:max_inf], label=str(prob))

print(max_inf)
plt.legend()
plt.grid(True)
plt.title("Percent of infected nodes (Square Latice)")
plt.xlabel("Time")
plt.ylabel("Average percent of nodes infected during simulation")


# In[214]:


#random graph
N=100 #overall population
p1=0.11 #probabillity of creation edge
I_random = np.random.randint(N) # randomly choosing first infected node


# In[217]:


#Loop for simulate on all of probabilities on list
for prob in probs:
    max_inf=0
    res=np.zeros(100)
    #100 times we simulate SIR model 
    for i in range (iters):
        G_random = nx.gnp_random_graph(N, p1)
        one_res = model_SIR_on_graph(G_random, I_random, prob)
        if one_res[2]>max_inf:
            max_inf=one_res[2]
        for i in range(len(one_res[0])):
            res[i] += one_res[0][i]/(N*iters)

    #Plot results
    plt.plot(t[:max_inf], res[:max_inf], label=str(prob))

print(max_inf)
plt.legend()
plt.grid(True)
plt.title("Percent of infected nodes (Random Graph)")
plt.xlabel("Time")
plt.ylabel("Average percent of nodes infected during simulation")


# In[218]:


#Watt-Strogatz graph
N = 100 #overall population
k = 5 #nomber of connections to of each node
p2 = 0.23 #probabillity of rewiring edge

I_watts = np.random.randint(N) # randomly choosing first infected node


# In[219]:


#Loop for simulate on all of probabilities on list
for prob in probs:
    max_inf=0
    res=np.zeros(100)
    #100 times we simulate SIR model 
    for i in range (iters):
        G_watts = nx.watts_strogatz_graph(N, k, p2)
        one_res = model_SIR_on_graph(G_watts, I_watts, prob)
        if one_res[2]>max_inf:
            max_inf=one_res[2]
        for i in range(len(one_res[0])):
            res[i] += one_res[0][i]/(N*iters)

    #Plot results
    plt.plot(t[:max_inf], res[:max_inf], label=str(prob))

print(max_inf)
plt.legend()
plt.grid(True)
plt.title("Percent of infected nodes (Watts-Strogatz Graph)")
plt.xlabel("Time")
plt.ylabel("Average percent of nodes infected during simulation")


# In[97]:


#Barabasi-Albert graph
m = 4 #connections with existing nodes
N = 100 #overall population
I_barabasi = np.random.randint(N) # randomly choosing first infected node


# In[220]:


#Loop for simulate on all of probabilities on list
for prob in probs:
    max_inf=0
    res=np.zeros(100)
    #100 times we simulate SIR model 
    for i in range (iters):
        G_random = nx.barabasi_albert_graph(N, m)
        one_res = model_SIR_on_graph(G_barabasi, I_barabasi, prob)
        if one_res[2]>max_inf:
            max_inf=one_res[2]
        for i in range(len(one_res[0])):
            res[i] += one_res[0][i]/(N*iters)

    #Plot results
    plt.plot(t[:max_inf], res[:max_inf], label=str(prob))

print(max_inf)
plt.legend()
plt.grid(True)
plt.title("Percent of infected nodes (Barabasi-Albert Graph)")
plt.xlabel("Time")
plt.ylabel("Average percent of nodes infected during simulation")


# ### TODO
# Discuss how the infection curves compare to the behavior seen in the
# ODE model.

# In[232]:


#Create list of probabilities and set number of iterations to 100
probs = np.arange(0.1, 1, 0.04)
iters = 100


# In[240]:


#square latice
m = 10 #overall population is equal m**2
res_latice = [] #Lists for results
tmr_latice = []
tmm_latice = []

#Loop for simulate on all of probabilities on list
for prob in probs:
    res=0
    tmm=0
    tmr=0
    #100 times we simulate SIR model 
    for i in range (iters):
        I_latice = (np.random.randint(m), np.random.randint(m))
        G_latice = nx.grid_2d_graph(m,m)
        one_res=model_SIR_on_graph(G_latice, I_latice, prob)
        res += one_res[1]
        tmm += one_res[2]
        tmr += one_res[3]
    #Append results to list
    res_latice.append(res/(iters*m**2))
    tmm_latice.append(tmm/iters)
    tmr_latice.append(tmr/iters)

#Plot results
plt.plot(probs, res_latice)
plt.grid(True)
plt.title("Percent of infected nodes (Square Latice)")
plt.xlabel("Probability of infection")
plt.ylabel("Average percent of nodes infected during simulation")


# In[241]:


plt.plot(probs, tmm_latice)
plt.grid(True)
plt.title("Average time of pandemic (Square Latice)")
plt.xlabel("Probability of infection")
plt.ylabel("Time")


# In[242]:


plt.plot(probs, tmr_latice)
plt.grid(True)
plt.title("Time when there were more nodes infected (Square Latice)")
plt.xlabel("Probability of infection")
plt.ylabel("Time")


# In[243]:


#random graph
N = 100 #overall population
p1 = 0.11 #probabillity of creation edge

res_latice = [] #Lists for results
tmr_latice = []
tmm_latice = []

#Loop for simulate on all of probabilities on list
for prob in probs:
    res=0
    tmm=0
    tmr=0
    #100 times we simulate SIR model 
    for i in range (iters):
        I_random = np.random.randint(N) 
        G_random = nx.gnp_random_graph(N,p1)
        one_res=model_SIR_on_graph(G_random, I_random, prob)
        res += one_res[1]
        tmm += one_res[2]
        tmr += one_res[3]
    #Append results to list
    res_latice.append(res/(iters*m**2))
    tmm_latice.append(tmm/iters)
    tmr_latice.append(tmr/iters)

#Plot results
plt.plot(probs, res_latice)
plt.grid(True)
plt.title("Percent of infected nodes (Random)")
plt.xlabel("Probability of infection")
plt.ylabel("Average percent of nodes infected during simulation")


# In[244]:


plt.plot(probs, tmm_latice)
plt.grid(True)
plt.title("Average time of pandemic (Random Graph)")
plt.xlabel("Probability of infection")
plt.ylabel("Time")


# In[245]:


plt.plot(probs, tmr_latice)
plt.grid(True)
plt.title("Time when there were more nodes infected (Random Graph)")
plt.xlabel("Probability of infection")
plt.ylabel("Time")


# #### TODO
# - Finish above task for different graphs
# - What each of the above measures tells you about the different networks?
# - Make gif

# In[ ]:

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

path = "C:\\Users\\Mateusz Kasprzak\\studia\\diffiuson processes\\assigment 4"

def barabasiAlbertGraph (N:int, M:list) -> nx.Graph:
    """
    Function creates Barabasi-Albert graph (new nodes are connected with "old" ones which has choosen proportionally to number of their neighbours).
    
    WARNING: function overwrite previously created graphs

    Arguments:
        N (int): Desired number of nodes.
        M (list): Not empty list of edges from which graph will grow.

    Return:
        graph (nx.Graph): created graph
    """
        
    #Creating an empty graph
    graph = nx.Graph()

    #Adding given edges to the graph.
    graph.add_edges_from(M)
    #Creating list of names of future nodes (it has to be longer than N, because some names can be already used)
    t=list(np.arange(N))
        
    #Redefining N as needed number of nodes
    N=N-len(graph.nodes)
        
    #Removing names which were used in the graph
    for vertices in graph.nodes:
        try:
            t.remove(vertices)
        except:
            pass

    #Taking needed number of names
    t=t[:N]

    #copyying list of nodes to not looping for changing object
    tempVar=list(graph.nodes())+[]
        
    #Adding edges to graph (every new node is connected with randomly chosen 
    #(with probability proportional to number of neighbors) node from list M)
    for i in range(N):
        for nds in tempVar:
            if np.random.random()<graph.degree(nds)/len(graph.edges):
                graph.add_edge(nds, t[i])
    return graph

def step (graph:nx.Graph, node:float|str)->float|str:
    """
    Function choosing node for next agent movement.

    Arguments:
        garph (nx.Graph): graph on which agent moving.
        node (float|str): node on which agent already is.

    Return:
        new_node (float|str): node on which agent will go after step
    """

    #Creating list to store neighbors list
    list_of_neighbors = []
    
    #Adding neighbors to list
    for neigh in graph.neighbors(node):
        list_of_neighbors.append(neigh)

    #Choosing next node which agent hit
    new_node = np.random.choice(list_of_neighbors)
    
    return new_node

def full_simulation (graph:nx.Graph, node:float|str, steps:int=20)->list:
    """
    """
    visited_nodes=[node]

    for i in range (steps):
        node = step(graph, node)
        visited_nodes.append(node)

    return visited_nodes

def save_gif(path:str, frames:int=5)->None:
    """
    Function to create GIF file from images
    
    Arguments:
    	path (str): path to folder where GIF may be saved
    	frames (int): number of frames in one minute

    Return:
        None
    """
    
    #Create list to store images
    images = []
    
    #Appending all of the images to list
    for files in os.listdir(f"{path}\\gif"):
        img = Image.open(f"{path}\\gif\\{files}")
        images.append(img)
    
    #Create the GIF file and save it.
    images[0].save(f"{path}\\animation_3.gif", append_images=images[1:], save_all=True, duration=len(images)/frames*60, loop=1)

#Creating emty list to store initial edges
M1=[]

#Adding randomly choosen initial edges to list
for i in range(13):
    for j in range(13):
        if i>j:
            p1=np.random.random()
            if p1<0.05:
                M1.append((i,j))

#Creating Barabasi Albert graph with 20 nodes
graph = barabasiAlbertGraph(20, M1)

#Set number of steps to 100
steps=100

#Running simulation
visited = full_simulation(graph, 2, steps)

#Creating list of all nodes
node_list=[]
for n in graph.nodes():
    node_list.append(n)

#Getting dictionary of possitions of nodes and edges
pos = nx.spring_layout(graph)

#Saving frames of simulation
for i in range (steps+1):
    #Draw all graph nodes with blue color
    nx.draw_networkx_nodes(graph, nodelist=node_list, pos=pos, node_color="blue", label="nodes", node_size=170)
    #Draw node with agent with green (owerdraw previous one)
    nx.draw_networkx_nodes(graph, pos=pos, node_color="green", nodelist=[visited[i]], label="agent", node_size=170)
    #Draw all edges
    nx.draw_networkx_edges(graph, edgelist=graph.edges(), pos=pos)
    #Create legend and title
    plt.legend(scatterpoints = True)
    plt.title(f"agent movement: {i}/{steps}")
    #Save figure and clear plot
    plt.savefig(f"{path}\\gif\\_{i+steps+1}.png")
    plt.cla()

#Running simulation with deafult parameters and save it to GIF
save_gif(path)

#Making simulation for 100 nodes
graph2 = barabasiAlbertGraph(100, M1)

#Creating list of all nodes
node_list2=[]
for n in graph2.nodes():
    node_list2.append(n)

#Set step number for 1000, and randomly choose origin node
steps2 = 1000
origin = np.random.choice(node_list2)

#Run simulation for second graph
visited2 = full_simulation(graph2, origin, steps2)

#Print number of hits for every node
for verts in graph2.nodes():
    if verts == origin:
        print(f"Node {verts} (origin) was hitted {visited2.count(verts)} times")
    else:
        print(f"Node {verts} was hitted {visited2.count(verts)} times")
print(f"Total number of hits equal {steps2+1}")

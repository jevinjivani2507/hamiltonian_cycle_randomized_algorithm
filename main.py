# importing all the required modules
from importlib.resources import path
import matplotlib.pyplot as plt
import numpy as np
import pylab
import random
import math
import os
import networkx as nx
from dataclasses import replace

from sympy import N

# checking for the valid number of vertices
isValid=0
while(isValid==0):
    number = int(input("Number of Vertices: "))
    if(number>3):
        isValid=1
    else:
        print("Please enter greater than 3 for interesting results.")

# taking all the edges
print("Enter list of edges: ")
edges=[]
x="0,0"


###  Taking input of graph to use.
invalid=0
completed=0
while(completed==0):

    invalid = 0

    x = (input().replace(" ","")).split(",")


    ## Data validation if edges have only vertices that actually exist.
    if(len(x)==1):
        completed = 1
        break
    if(len(x)==2):
        if(x[0]!=""): 
            x[0]=int(x[0])
        else:
            invalid=1
        if(x[1]!=""): 
            x[1]=int(x[1])
        else:
            invalid=1

    if(invalid==0 and completed==0):
        if(x[0]>=number or x[1]>=number or x[0]<0 or x[1]<0):
            print("please enter from existing vertices i.e. from 0 to ",(number-1),sep='')
            invalid=1
        elif(x!=""):
            ## Add edge to list if everything is right.
            edges.append(x)

print(edges)

### Adjacency graph of edges for faster computation.
print("Printing adjacency matrix of graph:")

mymat = []


### Create matrix of N x N with zeros
i=0
while(i<number):
    j=0
    newRow=[]
    while(j<number):
        newRow.append(0)
        j+=1
    mymat.append(newRow)
    i+=1


### Manually converting to adjacency matrix
for edge in edges:
    mymat[edge[0]][edge[1]] = 1
    mymat[edge[1]][edge[0]] = 1



###### Deprecated networkx function because of node number inconsistency.
# ### Using networkx library to convert from numpy Array
# adj=nx.to_numpy_matrix(nx.from_edgelist(np.array(edges)))
# print(adj)

### Convert Numpy array to Vanilla Python List.
adjList = mymat
print("From where do you want to start: ")
start = int(input())

def main():
    i = 0

    while i < number:
        i = i + 1
    # i=number
        if i > 3:
            ##generate random adjacency matrix of size ixi
            # adj = np.random.randint(0, 2, (i, i))
            # adj = adj
            # a random directed graph
            
            # from_numpy_matrix generate a graph from the given adjacency matrix
            G = nx.from_numpy_matrix(np.array(mymat))  # generator

            # adj = (nx.to_numpy_matrix(nx.from_edgelist(np.array(edges)))).tolist()
            # nx.draw(G,with_labels=True,font_color="whitesmoke")  # draw))
            
            print("Nodes of graph: ")
            print(G.nodes())
            print("Edges of graph: ")
            print(G.edges())
            A = adjList
            n = len(G.nodes)
            Visited = [False] * n
            Path = []

            def hamilton(curr):
                Path.append(curr)
                if len(Path) == n:
                    if A[Path[0]][Path[-1]] == 1:
                        return True
                    else:
                        Path.pop()
                        return False
                Visited[curr] = True

                ### Checking other nodes in order
                for next in range(n):
                    print(curr,next," does edge exist =",A[curr][next], " if visited =",Visited[next])

                    # print("A")
                    # print(A)
                    # print("A[curr]")
                    # print(A[curr])
                    # print("A[curr][next]")
                    # print(A[curr][next])
                    
                    if A[curr][next] == 1 and not Visited[next]:
                        if hamilton(next):
                            return True
                Visited[curr] = False
                Path.pop()

                return False

            # If it is hamiltonian graph
            # then we will print 
            if (hamilton(start)):
                Path.append(start)
                print("Hamiltonian Cycle Exists")    
                nx.draw(G,with_labels=True,font_color="whitesmoke")
                plt.annotate(str(Path),xy=(0,0))
                plt.show()
            else:
                print("Hamiltonian Cycle Doesn't Exists")
            
main()
import time
import matplotlib.pyplot as plt
import numpy as np
import pylab
import random
import math
import os
import networkx as nx
from dataclasses import replace


isValid=0
while(isValid==0):
    number = int(input("Number of Vertices: "))
    if(number>3):
        isValid=1
    else:
        print("Please enter greater than 3 for interesting results.")


start_time = time.time()


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

### Using networkx library to convert from numpy Array
adj=nx.to_numpy_matrix(nx.from_edgelist(np.array(edges)))
print(adj)

### Convert Numpy array to Vanilla Python List.
adjList = adj.tolist()


def main():
    i = 0

    while i < number:
        i = i + 1
    # i=number
        if i > 3:
            timeforprog = (time.time() - start_time)
            # adj = np.random.randint(0, 2, (i, i))
            # adj = adj
            # a random directed graph
            G = nx.from_numpy_matrix(adj)  # generator

            # adj = (nx.to_numpy_matrix(nx.from_edgelist(np.array(edges)))).tolist()
            nx.draw(G,with_labels=True,font_color="whitesmoke")  # draw))
            plt.show()
            print("Nodes of graph: ")
            print(G.nodes())
            print("Edges of graph: ")
            print(G.edges())
            A = adjList
            n = len(G.nodes)
            print(n)
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
                    print(next," does edge exist =",A[curr][next], " if visited =",Visited[next])

                    print("A")
                    print(A)
                    print("A[curr]")
                    print(A[curr])
                    print("A[curr][next]")
                    print(A[curr][next])
                    # print("A[curr][next][0]")
                    # print(A[curr][next][0])

                    if A[curr][next] == 1 and not Visited[next]:
                        if hamilton(next):
                            return True
                Visited[curr] = False
                Path.pop()

                return False


            print(hamilton(3))


            #  vremy = ['zero']
            # vershina = [0]
            # vremy.append(timeforprog)
            # vershina.append(n)
            # print(vremy)
            #  print(vershina)
            mainver = str(int(n))
            maintext = str(float(timeforprog))
            print("--- %s seconds ---" % (time.time() - start_time))
            # print(timeforprog)
            f2 = open('DataTime.txt','a')
            f2.write(maintext + os.linesep)
            f2.close()
            f3 = open('DataNodes.txt', 'a')
            f3.write(mainver + os.linesep)
            f3.close()
            f = open('Data.txt', 'a')
            f.write(maintext + '---' + mainver + ' Вершин' + os.linesep)
            f.close()

            

if __name__ == "__main__":
    main()
g = nx.Graph()
# g.add_edge_list(nx.transpose(nx.adj.nonzero()))



a = random.randint(1,50) # Generate Random Numbers
b = random.randint(1,50)

def proba(x,y):
    if x >y:
        return x
    else:
        return y
    print(proba(4,5))


# def hamilton(G, size, pt, path=[]):
#     print('hamilton called with pt={}, path={}'.format(pt, path))
#     if len(path)==size:
#         return path
#     for pt_next in G.get(pt, []):
#         res_path = [i for i in path]
#         if candidate is not None:  # skip loop or dead end
#             return candidate
#         print('path {} is a dead end'.format(path))
#     else:
#         print('pt {} already in path {}'.format(pt, path))

# print("Введите кол-во вершин")
# n = int(input())
# Visited = [False] * n
# Path = []

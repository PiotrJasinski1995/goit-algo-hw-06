import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



############# Task 1 #############
''' 
A - Dzierzoniow
B - Kolaczow
C - Niemcza
D - Jordanow
E - Cieszyce
F - Kobierzyce
G - Bielany_Wroclawskie
H - Wroclaw
'''

# assign data
mydata = [
    [1, 'A-B', 'Dzierzoniow-Kolaczow', 3],
    [2, 'A-C', 'Dzierzoniow-Niemcza', 4],
    [3, 'A-F', 'Dzierzoniow-Kobierzyce', 2],
    [4, 'B-D', 'Kolaczow-Jordanow', 1],
    [5, 'B-E', 'Kolaczow-Cieszyce', 1],
    [6, 'C-D', 'Niemcza-Jordanow', 3],
    [7, 'C-E', 'Niemcza-Cieszyce', 3],
    [8, 'C-G', 'Niemcza-Bielany_Wroclawskie', 2],
    [9, 'D-E', 'Jordanow-Cieszyce', 3],
    [10, 'E-F', 'Cieszyce-Kobierzyce', 2],
    [11, 'F-G', 'Kobierzyce-Bielany_Wroclawskie', 3],
    [12, 'F-H', 'Kobierzyce-Wroclaw', 3],
    [13, 'G-H', 'Bielany_Wroclawskie-Wroclaw', 3],
]

# Initializing graph
G = nx.Graph()

# Defining node positions
pos_dict = {'A': (0, 0), 'B': (2, 0), 'C': (3, 1.5), 'D': (3.5, 0.5), 'E': (5, 0), 'F': (6, -1), 'G': (7, 0), 'H': (9, 0)}

# Initializing edges and labels
edges = []
labels_dict = {}

# Assigning values to edges and labels
for data in mydata:
  edges_tuple = (data[1].split('-')[0], data[1].split('-')[1])
  edges.append(edges_tuple)
  labels_tuple = (data[1].split('-')[0], data[1].split('-')[1])

# Add edges to graph
G.add_edges_from(edges)

print('Nodes:', G.nodes(), sep='\n') 
print('Edges:', G.edges(), sep='\n')
print('Degree of nodes:', list(G.degree(G.nodes())), sep='\n')

nx.draw(G, pos=pos_dict, with_labels = True)
plt.show()

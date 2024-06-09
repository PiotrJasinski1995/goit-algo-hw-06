import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


############# Task 1 #############
''' 
0 - Dzierzoniow
1 - Kolaczow
2 - Niemcza
3 - Jordanow
4 - Cieszyce
5 - Kobierzyce
6 - Bielany_Wroclawskie
7 - Wroclaw
'''
# assign data
mydata = [
    [1, '0-1', 'Dzierzoniow-Kolaczow', 3],
    [2, '0-2', 'Dzierzoniow-Niemcza', 4],
    [3, '0-5', 'Dzierzoniow-Kobierzyce', 2],
    [4, '1-3', 'Kolaczow-Jordanow', 1],
    [5, '1-4', 'Kolaczow-Cieszyce', 1],
    [6, '2-3', 'Niemcza-Jordanow', 3],
    [7, '2-4', 'Niemcza-Cieszyce', 3],
    [8, '2-6', 'Niemcza-Bielany_Wroclawskie', 2],
    [9, '3-4', 'Jordanow-Cieszyce', 3],
    [10, '4-5', 'Cieszyce-Kobierzyce', 2],
    [11, '5-6', 'Kobierzyce-Bielany_Wroclawskie', 3],
    [12, '5-7', 'Kobierzyce-Wroclaw', 3],
    [13, '6-7', 'Bielany_Wroclawskie-Wroclaw', 3],
]

# # Forming adjacency matrix
# m_sm = [[0, 3, 4, 0, 0, 2, 0, 0],
#      [0, 0, 0, 1, 1, 0, 0, 0],
#      [0, 0, 0, 3, 3, 0, 2, 0],
#      [0, 0, 0, 0, 3, 0, 0, 0],
#      [0, 0, 0, 0, 0, 2, 0, 0],
#      [0, 0, 0, 0, 0, 0, 3, 3],
#      [0, 0, 0, 0, 0, 0, 0, 3],
#      [0, 0, 0, 0, 0, 0, 0, 0]]

# # Determining maximum and minimum time to complete each step
# q = []
# n_min = [0, 0, 0, 0, 0, 0, 0, 0]
# n_max = [0, 0, 0, 0, 0, 0, 0, 0]
# q.append(0)

# while len(q) > 0:
#   v = q.pop(0)

#   for i in range(len(m_sm[v])):
#     if m_sm[v][i] > 0:
#       q.append(i)
#       n_max[i] = n_max[v] + m_sm[v][i]

#       if n_min[i] == 0 or (n_min[i] > n_min[v] + m_sm[v][i]):
#         n_min[i] = n_min[v] + m_sm[v][i]

# print('n_min = ', n_min)
# print('n_max = ', n_max)

# Drawing directed graph
# Initializing graph
DG = nx.DiGraph()

# Defining node positions
pos_dict = {'0': (0, 0), '1': (2, 0), '2': (3, 1.5), '3': (3.5, 0.5), '4': (5, 0), '5': (6, -1), '6': (7, 0), '7': (9, 0)}

# Initializing edges and labels
edges = []
labels_dict = {}

# Assigning values to edges and labels
for data in mydata:
  edges_tuple = (data[1].split('-')[0], data[1].split('-')[1], data[3])
  edges.append(edges_tuple)
  labels_tuple = (data[1].split('-')[0], data[1].split('-')[1])
  labels_dict[labels_tuple] = f'w = {data[3]}'

# Add edges to graph
DG.add_weighted_edges_from(edges)

print('Nodes:', DG.nodes()) 
print('Edges:', DG.edges())
print('Degree of nodes:', list(DG.degree(DG.nodes())))

# Add color to the most critical path
color_edges = [('0', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7')]

nx.draw(DG, pos=pos_dict, with_labels = True)
nx.draw_networkx_edges(DG, edgelist = color_edges, pos=pos_dict, edge_color='red')
nx.draw_networkx_edge_labels(DG, pos=pos_dict, edge_labels=labels_dict)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt


def print_table(distances, visited):
    # Top row of the table
    print("{:<10} {:<10}".format("Vertex", "Distance"))
    print("-" * 20)
    
    # Data output for each vertex
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Yes" if vertex in visited else "Ні"
        print("{:<10} {:<10}".format(vertex, distance))


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
    # Outputting a table at the end
    print_table(distances, visited)

    return distances


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

# An example of a graph in the form of a dictionary
graph = {
    'A': {'B': 3, 'C': 4, 'F': 2},
    'B': {'A': 3, 'D': 1, 'E': 1},
    'C': {'A': 4, 'D': 3, 'E': 3, 'G': 2},
    'D': {'B': 1, 'C': 3, 'E': 3},
    'E': {'B': 1, 'C': 3, 'D': 3, 'F': 2},
    'F': {'A': 2, 'E': 2, 'G': 3, 'H': 3},
    'G': {'C': 2, 'F': 3, 'H': 3},
    'H': {'F': 3, 'G': 3},
}

# Calling the function for vertices
for vertice in graph:
    print(f'\nDistance table for vertice {vertice}:')
    dijkstra(graph, vertice)


# Initializing graph
G = nx.Graph()

# Defining node positions
pos_dict = {'A': (0, 0), 'B': (2, 0), 'C': (3, 1.5), 'D': (3.5, 0.5), 'E': (5, 0), 'F': (6, -1), 'G': (7, 0), 'H': (9, 0)}

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
G.add_weighted_edges_from(edges)

nx.draw(G, pos=pos_dict, with_labels = True)
nx.draw_networkx_edge_labels(G, pos=pos_dict, edge_labels=labels_dict)
plt.show()

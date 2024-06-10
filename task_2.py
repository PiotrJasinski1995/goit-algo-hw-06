from collections import deque


# DFS algorithm
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ') # Visit the vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# BFS algorithm
def bfs_recursive(graph, queue, visited=None):
    # Check if there is a set of visited vertices, if not, initialize a new one
    if visited is None:
        visited = set()
    # If the queue is empty, end the recursion
    if not queue:
        return
    # Remove the vertex from the beginning of the queue
    vertex = queue.popleft()
    # Check if this vertex has been visited before
    if vertex not in visited:
        # If not visited, output the vertex
        print(vertex, end=" ")
        # Add the vertex to the set of visited vertices.
        visited.add(vertex)
        # Add the unvisited neighbors of this vertex to the end of the queue.
        queue.extend(set(graph[vertex]) - visited)
    # Recursive function call with the same queue and set of visited vertices
    bfs_recursive(graph, queue, visited) 


# Representing a graph using an adjacency list
graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D', 'E', 'G'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D', 'C', 'F'],
    'F': ['A', 'E', 'G', 'H'],
    'G': ['C', 'H', 'F'],
    'H': ['F', 'G'],
}


# Calling the DFS function
print('Path from DFS algorithm:')
dfs_recursive(graph, 'A')


# Run the recursive BFS algorithm
print('\n\nPath from BFS algorithm:')
bfs_recursive(graph, deque(["A"]))

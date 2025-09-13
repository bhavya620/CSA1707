# BFS Implementation in Python using adjacency list

from collections import deque

def bfs(graph, start):
    visited = set()           # Keep track of visited nodes
    queue = deque([start])    # Use queue for BFS

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors that are not visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
bfs(graph, 'A')

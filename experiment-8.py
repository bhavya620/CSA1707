# DFS Implementation in Python using adjacency list

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        # Visit all neighbors recursively
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS
print("DFS Traversal:", end=" ")
dfs(graph, 'A')

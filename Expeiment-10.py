# A* Algorithm Implementation in Python

from queue import PriorityQueue

def a_star_search(graph, heuristics, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))   # (f, node)
    came_from = {}
    g = {node: float('inf') for node in graph}
    g[start] = 0

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_cost = g[current] + cost
            if new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + heuristics[neighbor]
                pq.put((f, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    return path, g[goal]


# Example graph (adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (estimated cost to goal 'G')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}

# Run A* search
path, cost = a_star_search(graph, heuristics, 'A', 'G')
print("Path found:", path)
print("Total cost:", cost)

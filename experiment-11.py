# Map Coloring Problem using CSP (Backtracking)

# Define the map (neighbors for each region)
neighbors = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "E"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["B", "C", "D"]
}

# Available colors
colors = ["Red", "Green", "Blue"]

# Dictionary to store color assignments
assignment = {}

# Function to check if current color is valid
def is_valid(node, color):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking CSP solver
def map_coloring(nodes):
    if not nodes:  # all nodes are assigned
        return True

    node = nodes[0]
    for color in colors:
        if is_valid(node, color):
            assignment[node] = color
            if map_coloring(nodes[1:]):
                return True
            assignment.pop(node)  # backtrack
    return False


# Run the CSP
nodes = list(neighbors.keys())
if map_coloring(nodes):
    print("Solution Found:")
    for region in assignment:
        print(region, "=>", assignment[region])
else:
    print("No solution found")

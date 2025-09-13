# Traveling Salesman Problem (Brute Force)

import itertools

# Example distance matrix (symmetric)
# Cities: 0, 1, 2, 3
# dist[i][j] = distance from city i to city j
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

num_cities = len(dist)
cities = range(num_cities)

min_path = None
min_cost = float('inf')

# Try all permutations of cities (except starting city 0)
for perm in itertools.permutations(cities[1:]):
    path = (0,) + perm + (0,)   # start and end at city 0
    cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))

    if cost < min_cost:
        min_cost = cost
        min_path = path

print("Optimal Path:", min_path)
print("Minimum Cost:", min_cost)

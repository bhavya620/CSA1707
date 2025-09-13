# Simple Vacuum Cleaner Problem

def vacuum_cleaner(world, start):
    score = 0
    location = start

    print("Initial World State:", world)

    for _ in range(len(world)):
        if world[location] == 1:
            print(f"Location {location} is Dirty. Cleaning...")
            world[location] = 0
            score += 1
        else:
            print(f"Location {location} is Already Clean.")

        # Move to next location
        location = (location + 1) % len(world)

    print("Final World State:", world)
    print("Performance Score:", score)


# 0 = Clean, 1 = Dirty
world = [1, 0, 1, 1]   # Example: 4 rooms
start_position = 0     # Start at Room 0

vacuum_cleaner(world, start_position)

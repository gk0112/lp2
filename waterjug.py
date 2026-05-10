from heapq import heappush, heappop

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
goal = int(input("Enter goal amount: "))

def heuristic(state):
    x, y = state
    return min(abs(x - goal), abs(y - goal))

def get_neighbors(state):
    x, y = state
    neighbors = []

    neighbors.append((jug1, y))
    neighbors.append((x, jug2))
    neighbors.append((0, y))
    neighbors.append((x, 0))

    transfer = min(x, jug2 - y)
    neighbors.append((x - transfer, y + transfer))

    transfer = min(y, jug1 - x)
    neighbors.append((x + transfer, y - transfer))

    return neighbors

def a_star():
    start = (0, 0)

    pq = []
    heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, current, path = heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        x, y = current

        if x == goal or y == goal:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heappush(pq, (new_f, new_g, neighbor, path))

    return None

solution = a_star()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found")

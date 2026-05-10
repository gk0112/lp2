from heapq import heappush, heappop

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start = []

print("Enter the initial state row by row:")
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star():
    pq = []

    heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, current, path = heappop(pq)

        current_tuple = state_to_tuple(current)

        if current_tuple in visited:
            continue

        visited.add(current_tuple)

        path = path + [current]

        if current == goal:
            return path

        for neighbor in get_neighbors(current):
            neighbor_tuple = state_to_tuple(neighbor)

            if neighbor_tuple not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heappush(pq, (new_f, new_g, neighbor, path))

    return None

solution = a_star()

if solution:
    print("\nSolution Path:\n")

    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")

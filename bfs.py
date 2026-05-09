def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    order = []
    step = 0

    print(f"\nStep 0: INIT     start = {start_node}")
    print(f"         Queue   : {queue}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    while queue:
        step += 1
        current_node = queue.pop(0)
        order.append(current_node)

        print(f"Step {step}: DEQUEUE  node = {current_node}")
        print(f"         Queue   : {queue}")
        print(f"         Visited : {sorted(visited)}")
        print(f"         Order   : {order}")
        print()

        for neighbor in graph[current_node]:
            step += 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                print(f"Step {step}: ENQUEUE  {current_node} → {neighbor} (unvisited, added to queue)")
            else:
                print(f"Step {step}: SKIP     {current_node} → {neighbor} (already visited)")

            print(f"         Queue   : {queue}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

    return order


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node {i+1}: ")
    
    neighbors = input(
        f"Enter neighbors of {node}: "
    ).split()

    graph[node] = neighbors

start_node = input("\nEnter starting node for BFS: ")

print("\n" + "=" * 50)
print("BFS TRAVERSAL — STEP BY STEP")
print("=" * 50)

result = bfs(graph, start_node)

print("=" * 50)
print(f"FINAL BFS ORDER: {result}")
print("=" * 50)
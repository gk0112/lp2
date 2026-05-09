from collections import deque

def dfs(graph, node, visited=None, order=None, stack=None, step=None):
    if visited is None:
        visited = set()
        order = []
        stack = []
        step = [0]

    step[0] += 1
    stack.append(node)
    visited.add(node)
    order.append(node)

    print(f"Step {step[0]}: VISIT    node = {node}")
    print(f"         Stack   : {stack}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    for neighbor in graph[node]:

        if neighbor not in visited:

            step[0] += 1

            print(f"Step {step[0]}: RECURSE  {node} → {neighbor} (unvisited, going deeper)")
            print(f"         Stack   : {stack}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

            dfs(graph, neighbor, visited, order, stack, step)

        else:

            step[0] += 1

            print(f"Step {step[0]}: SKIP     {node} → {neighbor} (already visited)")
            print(f"         Stack   : {stack}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

    stack.pop()

    step[0] += 1

    print(f"Step {step[0]}: RETURN   from {node} → back to {stack[-1] if stack else 'None (done)'}")
    print(f"         Stack   : {stack}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    return order



graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input(f"\nEnter node {i+1}: ")

    neighbors = input(
        f"Enter neighbors of {node} separated by space: "
    ).split()

    graph[node] = neighbors


start_node = input("\nEnter starting node for DFS: ")


print("\n" + "=" * 50)
print("DFS TRAVERSAL — STEP BY STEP")
print("=" * 50)
print()

result = dfs(graph, start_node)

print("=" * 50)
print(f"FINAL DFS ORDER: {result}")
print("=" * 50)
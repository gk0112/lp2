def print_colors(colors):
    print("Current Colors:", colors)
    print("-" * 25)

def is_safe(graph, colors, node, color):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, m, colors, node):
    if node == len(graph):
        print("Solution Found")
        print_colors(colors)
        return True

    for color in range(1, m + 1):
        print(f"Trying Color {color} for Node {node}")

        if is_safe(graph, colors, node, color):
            colors[node] = color

            print(f"Assigned Color {color} to Node {node}")
            print_colors(colors)

            if graph_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

            print(f"Backtracking from Node {node}")
            print_colors(colors)

    return False

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3

colors = [0] * len(graph)

graph_coloring(graph, m, colors, 0)

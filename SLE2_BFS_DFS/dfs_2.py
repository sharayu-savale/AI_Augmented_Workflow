import timeit

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X', 'Y'],
    'M': ['Z'],
    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}


def dfs(start, goal):
    stack = [start]
    visited = set([start])
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == goal:
            return nodes_explored

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return nodes_explored


execution_time = timeit.timeit(
    lambda: dfs('A', 'G'),
    number=100000
)

execution_time = (execution_time / 100000) * 1000

nodes = dfs('A', 'G')


print("DFS Version 2")
print("Start Node: A")
print("Goal Node: G")
print("Nodes Explored:", nodes)
print("Average Execution Time:", execution_time, "ms")
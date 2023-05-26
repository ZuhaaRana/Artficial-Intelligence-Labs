#BEST FIRST SEARCH ALGORITHM

#Value of heuristics
A = 40
B = 32
C = 25
D = 35
E = 19
F = 17
H = 10
G = 0

graph = 
{
    'A': [('B', B), ('C', C), ('D', D)],
    'B': [('E', E), ('A', A)],
    'C': [('E', E), ('F', F), ('A', A)],
    'D': [('A', A), ('F', F)],
    'E': [('C', C), ('B', B), ('H', H)],
    'F': [('G', G), ('D', D), ('C', C)],
    'G': [('F', F), ('H', H)],
    'H': [('E', E), ('G', G)]
}


def heuristic(path):
    value = 0
    for (node, cost) in path:
        value = cost
    return value, path[-1][0]

def BEST_FIRST_SEARCH(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        # Sort by cost
        queue.sort(key=heuristic)
        # Pop lowest cost
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print("Expanded path for Best First Search is : ", visited)
            return path
        else:
            adjacent = graph.get(node, [])
            for (node2, cost) in adjacent:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


sol = BEST_FIRST_SEARCH(graph, 'A', 'G')
print("Path along with costs is : ", sol)
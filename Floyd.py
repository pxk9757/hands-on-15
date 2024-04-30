def floyd_warshall(graph):
    distances = {i: {j: float('inf') for j in graph} for i in graph}
    for i in graph:
        distances[i][i] = 0
        for j in graph[i]:
            distances[i][j] = graph[i][j]

    for k in graph:
        for i in graph:
            for j in graph:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
                
    return distances

# Example usage:
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}
print(floyd_warshall(graph))

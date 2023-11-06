graph = {
    '7': [],
    '5': ['3', '7'],
    '3': ['2', '4'],
    '4': ['8'],
    '2': [],
    '8': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("The Depth-First Search for the graph is:")
dfs(visited, graph, '5')

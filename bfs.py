graph = {
    'A': ['B', 'C', 'D'],
    'C': ['A', 'E'],
    'B': ['A'],
    'D': ['A', 'E'],
    'E': []
}

def bfs(node):
    visited = [False] * (len(graph))  # Initialize a list to track visited nodes
    queue = []  # Initialize the queue for BFS
    visited.append(node)
    queue.append(node)
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)

# Driver Code
if __name__ == "__main__":
    print("The BFS traversal for the graph is:")
    bfs('A')

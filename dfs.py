class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_recursive(start, visited)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)

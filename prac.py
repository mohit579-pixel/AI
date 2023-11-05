def aStarAlgo(startnode, endnode):
    open_set = set([startnode])
    close_set = set()
    g = {}
    parent = {}
    g[startnode] = 0
    print(g[startnode])
    parent[startnode] = startnode
    while (len(open_set) > 0):
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == endnode or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in close_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n]+weight
                else:
                    if g[m]> g[n]+weight:
                        g[m] = g[n]+weight
                        parent[m] = n
                        if m in close_set:
                            open_set.add(m)
                            close_set.remove(m)
        if n is None:
            print('Path does not exist!')
            return None
        print(n)
        if n == endnode:
            path = []
            while parent[n]!=n:
                print(n)
                path.append(n)
                n = parent[n]
            path.append(startnode)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        close_set.add(n)
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

# Describe your graph here
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}
aStarAlgo('A', 'G')
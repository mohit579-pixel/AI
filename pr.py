
def astart(startnode,endnode):
    openset=set([startnode])
    closeset=set()
    g={}
    parent={}
    g[startnode]=0
    parent[startnode]=startnode
    while (len(openset)>0):
        n=None
        for v in openset:
            if n is None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        if n==endnode or Graph_nodes is None:
            pass
        else:
            for(m,weight) in get_neigh(n):
                openset.add(m)
                g[m]=g[n]+weight
                parent[m]=n
                













def get_neigh(v):
    if v in Graph_nodes:
        return Graph_nodes[v];
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
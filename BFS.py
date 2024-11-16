def BFS(source, graph):
    P = {}  # Padres
    Q = []  # cola (o pila en caso de DFS)

    Q.append(source)
    P[source] = None

    while Q:
        v = Q.pop(0)#Q.pop() para que sea una pila (DFS)
        for node in graph[v]:
            if node not in P.keys():
                P[node] = v
                Q.append(node)

    return P


G = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'E'], 'D': ['B'], 'E': ['C', 'F'], 'F': ['E']}

resultado = BFS('A', G)
print(resultado)

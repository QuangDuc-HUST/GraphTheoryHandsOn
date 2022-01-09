#
# We use list to represent queue
#

from DataStructures import Graph


def BFS(graph):
    """
    args:
        graph : Graph type
    return:
        Nothing, just print something important
    """

    visited = [0 for _ in range(graph.num_vertices())]
    d = [float('inf') for _ in range(graph.num_vertices())]
    pred = [None for _ in range(graph.num_vertices())]

    def BFS_mini(vertex):
        visited[vertex] = 1
        d[vertex] = 0
        pred[vertex] = None
        queue = []
        queue.append(graph.get_vertex(vertex))
        while len(queue):
            u = queue.pop(0)
            for ver in u.get_adjacenct_vertices():
                if not visited[ver.get_id()]:
                    visited[ver.get_id()] = 1
                    d[ver.get_id()] = d[u.get_id()] + 1
                    pred[ver.get_id()] = u.get_id()
                    queue.append(ver)
            print(u)

    

    for i in range(graph.num_vertices()):
        if not visited[i]:
            BFS_mini(i)

    return d , pred

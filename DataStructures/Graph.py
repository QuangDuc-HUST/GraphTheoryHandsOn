#
# Graph DS
#
# Interaction for outside world , use int or string only.
#
class AlreadySettingUp(Exception):
    pass


class Edge(object):
    def __init__(self, start, end, weight):
        self.__start = start
        self.__end = end
        self.__weight = weight

    def __repr__(self):
        return 'Edge {} -> {} : {}'.format(self.__start, self.__end, self.__weight)

    def __str__(self):
        return 'Edge {} -> {} : {}'.format(self.__start, self.__end, self.__weight)

    def _set_start_id(self, start):
        self.__start = start

    def get_start_id(self):
        return self.__start

    def _set_end_id(self, end):
        self.__end = end

    def get_end_id(self):
        return self.__end

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class Vertex(object):
    """
    Vertices in Graph
    """

    id = 0

    def __init__(self):
        self.__adj = []  # List of Vertices
        self.__id = Vertex.id
        self.__name = str(self.__id)
        Vertex.id += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_adjacenct_vertices(self):
        return self.__adj

    def _set_adjacent_vertices(self, lst):
        """
        Get list of Vertices type
        """
        self.__adj = lst[:]  # Copy

    def _append_adjacent_vertex(self, vertex):
        """
        Append a vertex in adjacent vertices
        """
        self.__adj.append(vertex) 

    def _delete_adjacent_vertex(self, vertex):
        self.__adj.remove(vertex)

    def __str__(self):
        """
        Print display
        """
        return f'Node {self.__name}'

    def __repr__(self):
        """
        List display
        """
        return f'Node {self.__name}'


class Graph(object):
    """
    Graph
    """

    def __init__(self, name='Franken'):
        self.__name = name
        self.__vertices = []  # List of vertices
        self.__edges = {} # List of edges 
        self.__isinit = False

    def get_name(self):
        return self.__name

    def get_list_of_vertices(self):
        return self.__vertices

    def get_list_of_edges(self):
        return self.__edges

    def num_vertices(self):
        return len(self.__vertices)

    def num_edges(self):
        return len(self.__edges)

    def _append_vertex(self, vertex):
        """
        vertex : Vertex type
        """
        self.__vertices.append(vertex)

    def _delete_vertex(self, vertex):
        """
        Costly , remove adj list, edge ...
        """
        pass

    def delete_vertex(self, vertex):
        pass

    def get_vertex(self, id):
        """
        id : int
        """
        return self.__vertices[id]


    def _append_edge(self, id, weight):
        """
        id : () tuple of 2 nodes
        weight : lu
        ??? existing edge ?
        """
        self.__edges[id] = Edge(*id, weight)
        start_vertex = id[0]
        start_vertex._append_adjacent_vertex(id[1])


    def delete_edge(self, start, end):
        """
        start: int
        end: int
        """
        start_vertex = self.get_vertex(start)
        end_vertex = self.get_vertex(end)
        del self.__edges[(start_vertex, end_vertex)]
        self.__vertices[start]._delete_adjacent_vertex(self.__vertices[end])
        self.__vertices[end]._delete_adjacent_vertex(self.__vertices[start])

    def get_edge(self, vertex1, vertex2):
        """
        vertex1: int
        vertex2: int
        """
        return self.__edges[(self.get_vertex(vertex1), self.get_vertex(vertex2))]


    def initialization(self, ADJ_matrix, num_V, kind = 'Adj'):
        """
        Setting up Graph
        ADJ: adjacency list corresponding to V
        num_V : int
        """

        if self.__isinit:
            raise AlreadySettingUp()

        if kind == 'Adj':
            self.__isinit = True
            for i in range(num_V):
                self._append_vertex(Vertex())

            for i in range(num_V):
                for j in range(num_V):
                    if ADJ_matrix[i][j]:
                        self._append_edge((self.__vertices[i], self.__vertices[j]), ADJ_matrix[i][j])


if __name__ == '__main__': 
    # Testing

    # path = 'C:\\Users\\Franken\\PycharmProjects\\nqd_colab_1\\GraphTheoryHandsOn\\sampledata.txt'
    path = r'D:\GraphTheoryHandsOn\sampledata_adjacencymatrix.txt'
    with open(path) as f:
        n = int(f.readline())
        adj_matrix = []
        for i in range(n):
            line = list(map(int, f.readline().split()))
            adj_matrix.append(line)

    ADJ = adj_matrix

    LL = Graph()
    LL.initialization(ADJ, n)
    print(LL.get_list_of_vertices())
    print(LL.get_list_of_edges())
    print(LL.num_edges())
    print(LL.num_vertices())
    print(LL.get_vertex(0))
    print(LL.get_edge(2, 3))
    print(LL.get_vertex(2).get_adjacenct_vertices())
    print('Delete edge 2 -> 3')
    LL.delete_edge(2, 3)
    print(LL.get_list_of_edges())
    print(LL.get_vertex(2).get_adjacenct_vertices())
import sys

class AlreadySettingUp(Exception):
    pass


class Vertex(object):
    '''
    Nodes in Graph
    '''
    id = 0

    def __init__(self):
        self.__adj = []  ## List of Vertices
        self.__id = Vertex.id
        self.__name = str(self.__id)
        Vertex.id += 1

    def get_name(self):
        return self.__name

    def set_name(self , name):
        self.__name = name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight
        
    def get_id(self):
        return self.__id

    def reset_id(self):
        '''
        Reset id node
        '''
        Vertex.id = 0

    def get_adjacenct_vertices(self):
        return self.__adj
    
    def set_adjacent_vertices(self, lst):
        '''
        Get list of Vertices type
        '''
        self.__adj  = lst[:] ## Copy 

    def append_adjacent_nodes(self, vertex):
        '''
        Append a vertex in adjacent vertices
        '''
        self.__adj.append(vertex) ## Not copy

    def __str__(self):
        '''
        Print display
        '''
        return f'Node {self.__name}'
    
    def __repr__(self) :
        '''
        List display
        '''
        return f'Node {self.__name}'

class Graph(object):
    '''
    Graph
    '''

    def __init__(self, name = 'Franken'):
        self.__name = name
        self.__vertices = []  ## List of Vertices types
        self.__isinit = False

    def num_vertices(self):
        return len(self.__vertices)

    def append_vertices(self, vertex):
        '''
        vertex : Vertex type
        '''
        self.__vertices.append(vertex)
    
    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, lst):
        '''
        lst  : list of vertices
        '''
        self.__vertices = lst
    

    def initialization(self, ADJ_matrix, num_V):
        '''
        Setting up Graph
        ADJ: adjacency list corresponding to V
        Do not have weight
        '''
        if self.__isinit:
            raise AlreadySettingUp()
        else:
            self.__isinit = True

        ### Init vertices

        #############
        num_V = len(num_V)
        ############

        for i in range(num_V):
            self.append_vertices(Vertex())


        for i in range(num_V):
            for j in range(num_V):
                if ADJ_matrix[i][j]:
                    self.__vertices[i].append_adjacent_nodes(self.__vertices[j])


        


    def get_name(self):
        return self.__name

    def get_listvertices(self):
        return self.__vertices
    


# class Graph:
# 	def __init__(self, adj_matrix, vertices):
# 		self.vertices = vertices
# 		self.adj_of_vertices = {i: [] for i in self.vertices}
# 		self.edges = {}
# 		for i in range(len(self.vertices)):
# 			for j in range(len(self.vertices)):

# 				if adj_matrix[i][j] != 0:
# 					self.edges[self.vertices[i], self.vertices[j]] = adj_matrix[i][j]

# 					if i not in self.adj_of_vertices[j]:
# 						self.adj_of_vertices[j].append(i)

# 					if j not in self.adj_of_vertices[i]:
# 						self.adj_of_vertices[i].append(j)

# 		self.cycle = False

# 	def get_edges(self):
# 		return self.edges

# 	def get_adj(self, x):
# 		print(self.adj_of_vertices)
# 		return self.adj_of_vertices[x]

# 	def check_cycle(self):
# 		pass



if __name__ == '__main__': 
    ## Testing
    print('Hello')

        
    # path = 'C:\\Users\\Franken\\PycharmProjects\\nqd_colab_1\\GraphTheoryHandsOn\\sampledata.txt'
    path = r'D:\GraphTheoryHandsOn\sampledata.txt'
    with open(path) as f:
        n = int(f.readline())
        adj_matrix = []
        for i in range(n):
            line = list(map(int, f.readline().split()))
            adj_matrix.append(line)

    V = [i for i in range(n)]
    ADJ = adj_matrix

    LL = Graph()
    LL.initialization(ADJ, V)
    # print(LL.get_edges())
    # print(LL.get_adj(1))


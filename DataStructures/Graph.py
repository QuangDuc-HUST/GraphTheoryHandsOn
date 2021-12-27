import sys

class AlreadySettingUp(Exception):
    pass


class Node(object):
    '''
    Nodes in Graph
    '''
    id = 0

    def __init__(self, weight):
        self.__adj = []  ## List of Nodes
        self.__id = Node.id
        self.__name = str(self.__id)
        self.__weight = weight
        Node.id += 1

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
        Node.id = 0

    def get_adjacenct_nodes(self):
        return self.__adj
    
    def set_adjacent_nodes(self, lst):
        '''
        Get list of Node type
        '''
        self.__adj  = lst[:] ## Copy 

    def append_adjacent_nodes(self, node):
        '''
        Append a node in adjacent nodes
        '''
        self.__adj.append(node) ## Not copy

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
    def __init__(self, name):
        self.__name = name
        self.__nodes = []  ## List of Node types
        self.__isinit = False
    
    def getadjacentmatrix(self, data):
        '''
        Setting up Graph
        '''
        if self.__isinit:
            raise AlreadySettingUp()
        else:
            self.__isinit = True



    def get_name(self):
        return self.__name

    def get_listnodes(self):
        return self.__nodes
    


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
    a = Node()
    b = Node()
    print(a.get_id())
    print(b.get_id())

        
    # path = 'C:\\Users\\Franken\\PycharmProjects\\nqd_colab_1\\GraphTheoryHandsOn\\sampledata.txt'
    # with open(path) as f:
    #     n = int(f.readline())
    #     adj_matrix = []
    #     for i in range(n):
    #         line = list(map(int, f.readline().split()))
    #         adj_matrix.append(line)

    # V = [i for i in range(n)]
    # ADJ = adj_matrix

    # LL = Graph(ADJ, V)
    # print(LL.get_edges())
    # print(LL.get_adj(1))


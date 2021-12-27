class AlreadySettingUp(Exception):
    pass


class Node(object):
    '''
    Nodes in Graph
    '''
    id = 0

    def __init__(self):
        self.__adj = []  ## List of Nodes
        self.__id = Node.id
        self.__name = str(self.__id)
        Node.id += 1

    def get_name(self):
        return self.__name

    def set_name(self , name):
        self.__name = name

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
    
     



if __name__ == '__main__': 
    ## Testing
    print('Hello')
    a = Node()
    b = Node()
    print(a.get_id())
    print(b.get_id())

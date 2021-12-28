class Node:
    def __init__(self, id):
        self.__id = id
        self.__parent = None
        self.__children = {}
        self.__weight = None

    def __repr__(self):
        return 'Node ' + str(self.__id)
        
    def get_id(self):
        return self.__id

    def set_parent(self, parent):
        self.__parent = parent

    def get_parent(self):
        return self.__parent

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def all_new_children(self, children):
        self.__children = children

    def append_child(self, child: 'Node'):
        self.__children[child.get_id()] = child

    def change_child(self, old: 'Node', new: 'Node'):
        self.__children[old.get_id()] = new

    def get_children(self):
        return self.__children


class Tree:
    def __init__(self):
        self.__root = None


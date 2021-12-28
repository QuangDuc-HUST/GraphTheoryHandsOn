#
# Graph DS
#
class AlreadySettingUp(Exception):
	pass


class Edge:
	def __init__(self, start, end, weight):
		self.__start = start
		self.__end = end
		self.__weight = weight

	def __repr__(self):
		return 'Edge from {} to {}'.format(self.__start, self.__end)

	def __str__(self):
		return 'Edge from {} to {}'.format(self.__start, self.__end)

	def set_start_id(self, start):
		self.__start = start

	def get_start_id(self):
		return self.__start

	def set_end_id(self, end):
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
		self.__weight = None
		Vertex.id += 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_weight(self):
		return self.__weight

	def set_weight(self, weight):
		self.__weight = weight

	def get_id(self):
		return self.__id

	def get_adjacenct_vertices(self):
		return self.__adj

	def set_adjacent_vertices(self, lst):
		"""
		Get list of Vertices type
		"""
		self.__adj = lst[:]  # Copy

	def append_adjacent_vertex(self, vertex):
		"""
		Append a vertex in adjacent vertices
		"""
		self.__adj.append(vertex)  # Not copy

	def delete_adjacent_vertex(self, vertex):
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
		# Change vertices to dict (like hash table) 
		self.__vertices = []  # List of Vertices types
		self.__edges = {}
		self.__isinit = False

	def get_name(self):
		return self.__name

	def get_list_of_vertices(self):
		return self.__vertices

	def get_list_of_edges(self):
		return self.__edges


	def num_vertices(self):
		return len(self.__vertices)


	def append_vertices(self, vertex):
		"""
		vertex : Vertex type
		"""
		self.__vertices.append(vertex)

	def delete_vertices(self, vertex):
		"""
		Costly , remove adj list, edge ...
		"""
		pass

	def append_edges(self, id, weight):
		"""
		id : [] list of 2 nodes
		weight : lu
		"""
		self.__edges[id] = Edge(*id, weight)


	def delete_edge(self, start, end):
		del self.__edges[(start, end)]
		self.__vertices[start].delete_adjacent_vertex(self.__vertices[end])
		self.__vertices[end].delete_adjacent_vertex(self.__vertices[start])

	def get_vertices(self):
		return self.__vertices

	def set_vertices(self, lst):
		"""
		lst  : list of vertices
		"""
		self.__vertices = lst

	def initialization(self, ADJ_matrix, num_V):
		"""
		Setting up Graph
		ADJ: adjacency list corresponding to V
		num_V : int
		"""

		if self.__isinit:
			raise AlreadySettingUp()
		else:
			self.__isinit = True


		for i in range(num_V):
			self.append_vertices(Vertex())

		for i in range(num_V):
			for j in range(num_V):
				if ADJ_matrix[i][j]:
					# adding adj
					self.__vertices[i].append_adjacent_vertex(self.__vertices[j])

					# adding edge
					self.append_edges((self.__vertices[i], self.__vertices[j]), ADJ_matrix[i][j])


if __name__ == '__main__': 
	# Testing
	print('Hello, Trang lu Van Anh Ngan')

	# path = 'C:\\Users\\Franken\\PycharmProjects\\nqd_colab_1\\GraphTheoryHandsOn\\sampledata.txt'
	path = r'D:\GraphTheoryHandsOn\sampledata.txt'
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

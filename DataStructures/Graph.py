import sys


class Node:
	def __init__(self, id, weight):
		self.id = id
		self.weight = weight


	def get_id(self):
		return self.id

	def get_weight(self):
		return self.weight


class Graph:
	def __init__(self, adj_matrix, vertices):
		self.vertices = vertices
		self.adj_of_vertices = {i: [] for i in self.vertices}
		self.edges = {}
		for i in range(len(self.vertices)):
			for j in range(len(self.vertices)):

				if adj_matrix[i][j] != 0:
					self.edges[self.vertices[i], self.vertices[j]] = adj_matrix[i][j]

					if i not in self.adj_of_vertices[j]:
						self.adj_of_vertices[j].append(i)

					if j not in self.adj_of_vertices[i]:
						self.adj_of_vertices[i].append(j)

		self.cycle = False

	def get_edges(self):
		return self.edges

	def get_adj(self, x):
		print(self.adj_of_vertices)
		return self.adj_of_vertices[x]

	def check_cycle(self):
		pass


path = 'C:\\Users\\Franken\\PycharmProjects\\nqd_colab_1\\GraphTheoryHandsOn\\sampledata.txt'
with open(path) as f:
	n = int(f.readline())
	adj_matrix = []
	for i in range(n):
		line = list(map(int, f.readline().split()))
		adj_matrix.append(line)

V = [i for i in range(n)]
ADJ = adj_matrix

LL = Graph(ADJ, V)
print(LL.get_edges())
print(LL.get_adj(1))

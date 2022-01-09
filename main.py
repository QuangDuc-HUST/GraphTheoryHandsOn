#
# Just for fun
#
from Algorithms import BFS_QD
from DataStructures.Graph import Graph


if __name__ == '__main__':
    path = r'D:\GraphTheoryHandsOn\sampledata_adjacencymatrix.txt'
    with open(path) as f:
        n = int(f.readline())
        adj_matrix = []
        for i in range(n):
            line = list(map(int, f.readline().split()))
            adj_matrix.append(line)

    ADJ = adj_matrix
    LL = Graph()
    LL.init_adj(n, ADJ)
    d, pred = BFS_QD.BFS(LL)
    print(pred, d)
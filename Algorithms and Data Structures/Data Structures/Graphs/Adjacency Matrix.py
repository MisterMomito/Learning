class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex  # 1
            # for loop appends a column of zeros to the edges matrix
            for row in self.edges:  # 2
                row.append(0)
            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0] * (len(self.edges) + 1))  # 3  appends 0's like this: [0, 0, 0]
            self.edge_indices[vertex.name] = len(self.edge_indices)  # 4  stores the actual indices example name: 0
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:  # 1
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight  # 2 no err. #3 adds 1
            #           ^ calls name, key to index
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            #  ^ these are doing [index1][index2] = weight. Remember each index corresponds to a name as per ed_indices
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):  # v is name, i is index of vertex placement
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')

'''
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
'''


g = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)

g.add_edge('A', 'C')
g.print_graph()



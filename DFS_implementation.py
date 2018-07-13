from collections import defaultdict
# The class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        # The strength of deafult dict even if there are no keys it will add keys automatically and will not return key error
        self.graph = defaultdict(list)  # default dictionary to store graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printgraph(self):
        print(self.graph)
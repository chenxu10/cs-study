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

    # Use BFS to check path between s and d
    def isReachable(self, s, d):
        # mark all the vertices as not visited
        visited = [False] * (self.V)
        # create a queue for BFS
        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from queue
            n = queue.pop(0)

            # if the adjacaent node is the desitination node, then return True
            if n == d:
                return True

            # else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False
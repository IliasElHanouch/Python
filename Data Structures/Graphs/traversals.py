from graph import Graph
class GraphTraversals(Graph):
    def _bfs(self,vertex: object,visited:dict):
        #We use a queue to queue and dequeue the vertices, starting from vertex which is
        #visited too
        queue = [vertex]
        visited[vertex] = True
        while len(queue) >0:
            #We dequeue it
            v = queue.pop(0)
            #print(v,end=" ")
            #We check its adjacents and add them if not visited
            for adj in self._vertices[v]:
                if not visited[adj.vertex]:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True
    
    def bfs(self):
        "It returns the BFS traversal printing all the vertices"
        print("BFS traversal is: ")
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        for vertex in self._vertices.keys():
            if not visited[vertex]:
                self._bfs(vertex,visited)
    
    def _dfs_it(self,vertex,visited):
        """Iterative method for DFS"""
        #We use a stack for this method
        stack = [vertex]
        visited[vertex] = True

        while len(stack) > 0:
            v = stack.pop()
            print(v,end=" ")

            for adj in reversed(self._vertices[v]):
                if not visited[adj.vertex]:
                    stack.append(adj.vertex)
                    visited[adj.vertex] = True
    
    def _dfs(self,vertex,visited):
        "Recursive method for DFS"
        visited[vertex] = True
        print(vertex,end= " ")
        #If ajdacent vertices are not visited
        for adj in self._vertices[vertex]:
            #We call the recurive method for dfs
            if not visited[adj.vertex]:
                self._dfs(adj.vertex,visited)

    
    def dfs(self):
        print("DFS Traversal is: ")
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        for vertex in self._vertices.keys():
            if not visited[vertex]:
                self._dfs(vertex,visited)
    
    #Optional method: we get the reachables vertices from a vertex
    def getReachable(self,vertex):
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        self._bfs(vertex,visited)
        res = []
        for vert in self._vertices.keys():
            if visited[vert] and vert != vertex:
                res.append(vert)
        print("Reachable vertices from {} are: {}".format(vertex,res))
    
    #Optional method: we get the non-accessible vertices from a vertex
    def getnonAccessible(self,vertex):

        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        self._dfs(vertex,visited)
        res = []
        for vert in self._vertices.keys():
            if not visited[vert]:
                res.append(vert)
        print("Non accessible vertices from {} are: {}".format(vertex,res))
labels = ["A","B","C","D","E","F"]
g = GraphTraversals(labels)
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("A","D")
g.add_edge("E","A")
#g.bfs()
g.getReachable("A")
g.dfs()
g.getnonAccessible("C")

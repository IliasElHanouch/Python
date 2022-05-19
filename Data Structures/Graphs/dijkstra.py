import sys
class AdjacentVertex:
    """ This class allows us to represent a tuple
    with an adjacent vertex
    and the weight associated (by default None, for non-unweighted graphs)"""
    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (vertex, weight)"""
        return '(' + str(self.vertex) + ',' + str(self.weight) + ')'

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.vertex == other.vertex and self.weight == other.weight
class Graph:
    def __init__(self, vertices: list, directed: bool = True) -> None:
        """ We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
        self._directed = directed
    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n'+str(v)+':'
            for adj in self._vertices[v]:
                result += str(adj)+"  "
        return result

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neighbours for start
        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            # adds to the end of the list of neighbors for end
            self._vertices[end].append(AdjacentVertex(start, weight))

    """Dijkstra's algorithm adapted to Python with dictionary-based implementation"""
    #Let's define de minimum distance algorithm
    def minDistance(self,visited: dict, distances: dict):
        """It returns the vertex with minimum distance"""
        #There is no min vertex nor minimum distance at the beginning
        min_vertex = None
        min = sys.maxsize
        #We update the minimum distance and min vartex
        for v in self._vertices.keys():
            if distances[v] <= min and not visited[v]:
                min = distances[v]
                min_vertex = v
        return min_vertex
    
    def dijkstra(self,start):
        "Dijkstra's algorithm to obtain the minimum path from a vertex to the rest in the graph"
        #Dictionaries to store distances, visited and previous vertices
        distances = {}
        visited = {}
        previous = {}
        for v in self._vertices.keys():
            distances[v] = sys.maxsize
            visited[v] = False
            previous[v] = None
        #Now we start
        distances[start] = 0 #Vertex's distance with itself is 0
        
        for _ in range(len(self._vertices.keys())):
            #We obtain the min distance vertex
            u = self.minDistance(visited,distances)
            #And we marked it as visited
            visited[u] = True
            #And we check/update its adjacents conditions
            for adj in self._vertices[u]:
                i = adj.vertex
                w = adj.weight
                #We compare its distance and the previous (plus the previous one too) in order to replace it
                if not visited[i] and distances[i] > distances[u] + w:
                    distances[i] = distances[u] + w
                    previous[i] = u
        return distances,previous
    
    def minimum_path(self,start,end):
        "It checks if there is a minimum path between 2 vertices, and if it is case, print it"
        #Excepctions
        if start is None or end is None or start not in self._vertices.keys() or end not in self._vertices.keys():
            return None, None
        distances,previous = self.dijkstra(start)
        if distances[end] == sys.maxsize:
            return [],float("inf")
        #We add end to result, and we will insert previous vertices (reversed path)
        result = [end]
        #We star from previous vertex
        prev = previous[end]
        while prev != None:
            result.insert(0,prev)
            prev = previous[prev]
        #We return the path and the distance
        return("Minimum path from {} to {} is: {}. Distance: {}".format(start,end,result,distances[end]))


"""Example"""
labels = ['S','B','C','D','E','T']
g= Graph(labels,True)
g.add_edge('S','B',4)
g.add_edge('C','S',2)
g.add_edge('D','B',5)
g.add_edge('E','D',2)
g.add_edge('C','E',10)
g.add_edge('D','T',6)
g.add_edge('B','C',1)
g.add_edge('C','D',8)
g.add_edge('E','T',3)
#g.dijkstra('S')
print(g)
print(g.minimum_path('S','T'))

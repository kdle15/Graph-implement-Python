from structures.graph import Graph
class DirectedGraph(Graph):
    def __init__(self,vertices, edges):
        self.vertices = vertices
        self.edges = edges

        # Also construct neighbor sets
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for edge in edges:
            (u, v) = (edge[0], edge[1])
            self.neighbors[u].add(v)

    def isSource(self,v):
        neighbors = set()
        for u in self.vertices:
            neighbors |= self.neighbors[u]
        return v not in neighbors

    def findSource(self):
        for v in self.vertices:
            if self.isSource(v):
                return v

    def topsort(self):
        order = list()
        while len(self.vertices) > 0:
            v = self.findSource()
            if v is None:
                return None
            self.vertices.remove(v)
            self.neighbors.pop(v)
            order.append(v)
        return order

def test():
    vertices = {1, 2, 3, 4, 5, 6}
    edges = {(1,2), (2,3), (3,5), (5, 4), (5,6)}
    graph = DirectedGraph(vertices, edges)

    #topsoer
    print(graph.topsort())

if __name__ == '__main__':
    test()
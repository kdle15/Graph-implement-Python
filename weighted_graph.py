from structures.graph import Graph
import heapq
class WeightedGraph(Graph):

    def __init__(self, vertices, edges):
        # Save the original sets
        self.vertices = vertices
        self.edges = edges

        # Also construct neighbor sets
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for (u, v, w) in edges:
            self.neighbors[u].add(v)
            self.neighbors[v].add(u)

        self.weight = dict()
        for(u,v,w) in edges:
            self.weight[(u,v)] = w
            self.weight[(v,u)] = w

    def dijkistra(self,v):
        parents = {v: v}
        costs = {v: 0}
        frontier = [(0,v)]
        while(len(frontier) > 0):
            (pcost,p) = heapq.heappop(frontier)
            # ignore the repeate
            if pcost == costs[p]:
                for c in self.neighbors[p]:
                    d = pcost + self.weight[(p,c)]
                    #if c not in parents or costs[c] > d:
                    if c not in parents:
                        parents[c] = p
                        costs[c] = d
                        heapq.heappush(frontier,(d,c))
                    elif costs[c] > d:
                        parents[c] = p
                        costs[c] = d
                        #update c priority to d
                        heapq.heappush(frontier,(d,c))
        return parents

    # Return the total weight along this path in this graph.
    # path = deque of vertices
    def path_weight(self, path):
        total = 0
        v = None
        for u in path:
            if v is None:
                v = u
            else:
                total += self.weight[(v, u)]
                v = u
        return total

    # Return a dictionary representing a minimum spanning tree.
    # v = root vertex for the MST
    def prim(self, v):
        finish = set()
        parent = {v:v}
        cost = {v:0}
        frontier = [(0, v)]
        while(len(frontier) > 0):
            (pcost,p) = heapq.heappop(frontier)
            finish.add(p)
            for c in self.neighbors[p]:
                w = self.weight[(p,c)]
                if c not in finish:
                    if c not in parent or cost[c] > w:
                        parent[c] = p
                        cost[c] = w
                        heapq.heappush(frontier,(w,c))
        return parent

    # Convert a tree from dictionary form into a set of edges.
    # parents = the dictionary representation
    def tree(self, parents):
        setofedges = set()
        for vertex in parents.keys():
            if (vertex != parents[vertex]):
                setofedges.add((vertex, parents[vertex], self.weight[(vertex,parents[vertex])]))
        return setofedges

# FILL THIS IN
def test():
    vertices = {'A','B', 'C', 'D', 'E'}
    edges = {('A','B', 4),('B','D', 3),('B','C', 1),('C','E', 6),('D','E', 1),('A','C', 2)}
    graph = WeightedGraph(vertices, edges)

    parents = graph.prim('A')
    trees = graph.tree(parents)
    print(trees)
    for v in graph.vertices:
        path = Graph.path(v, parents)
        print(v, path, graph.path_weight(path))



if __name__ == '__main__':
    test()
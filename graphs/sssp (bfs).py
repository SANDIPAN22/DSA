from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self, source, desti):
        self.graph[source].append(desti)

    def sssp(self, source, desti):
        self.q=[[source]]
        

        while len(self.q):
            print(self.q)
            path=self.q.pop(0)
            node=path[-1]
            if node==desti:
                return path
            else:
                for k in self.graph[node]:
                    
                    n_path=list(path)
                    print('path==>> ',n_path)
                    n_path.append(k)
                    self.q.append(n_path)
                    

g=Graph()
g.addEdge('a','b')
g.addEdge('a','c')
g.addEdge('b','d')
g.addEdge('b','g')
g.addEdge('c','d')
g.addEdge('c','e')
g.addEdge('d','f')
g.addEdge('e','f')
g.addEdge('g','f')
print(g.graph)

print(g.sssp('g','a'))












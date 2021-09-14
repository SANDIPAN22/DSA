from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
       
        self.nodes=[]
    def addEdge(self,source,desti):
        
        if source not in self.nodes:
            self.nodes.append(source)
        if desti not in self.nodes:
            self.nodes.append(desti)
        self.graph[source].append(desti)
    def topologyUtil(self,v,visited,stak):
        visited.append(v)
        for k in self.graph[v]:
            if k not in visited:
                self.topologyUtil(k,visited,stak)
        stak.append(v)
    def topology(self):
        visited=[]
        stak=[]
        print(self.nodes)
        for n in self.nodes:
            if n not in visited:
                self.topologyUtil(n,visited,stak)
        print(stak[::-1])

        
g= Graph()
g.addEdge('f', 'c')
g.addEdge('f', 'a')
g.addEdge('e', 'a')
g.addEdge('e', 'b')
g.addEdge('c', 'd')
g.addEdge('d', 'b')

print(g.graph)

g.topology()
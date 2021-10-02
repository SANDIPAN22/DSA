import sys
from collections import defaultdict
inf=sys.maxsize
class Graph:
    def __init__(self,node_no):
        self.graph=defaultdict(list)
        self.nn=node_no
        self.nodes={}
        self.edges=[]
    def addEdge(self,source,desti,cost):
        data={'src':source,'desti':desti,'cost':cost}
        self.edges.append(data)
        self.graph[source].append((cost,desti))
        if source not in self.nodes.keys():
            self.nodes[source]={'wt':inf,'pred':''}
        if desti not in self.nodes.keys():
            self.nodes[desti]={'wt':inf,'pred':''}
    def sssp(self,start,end):
        self.nodes[start]['wt']=0

        for k in range(self.nn-1):
            for j in self.edges:
                
                if self.nodes[j['src']]['wt']+j['cost']< self.nodes[j['desti']]['wt']:
                    self.nodes[j['desti']]['wt']=self.nodes[j['src']]['wt']+j['cost']
                    self.nodes[j['desti']]['pred']=j['src']

g=Graph(5)
g.addEdge('a','c',6)
g.addEdge('a','d',6)
g.addEdge('b','a',3)
g.addEdge('c','d',1)
g.addEdge('d','c',2)
g.addEdge('d','b',1)
g.addEdge('e','b',4)
g.addEdge('e','d',2)

g.sssp('e','a')

print(g.nodes)
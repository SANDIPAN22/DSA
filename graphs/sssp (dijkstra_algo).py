import heapq
from collections import defaultdict
import sys
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.nodes={}
    def addEdge(self,source,desti,cost):
        inf=sys.maxsize
        self.graph[source].append((cost,desti))
        if source not in self.nodes.keys():
            self.nodes[source]={'wt':inf,'pred':''}
        if desti not in self.nodes.keys():
            self.nodes[desti]={'wt':inf,'pred':''}

    def genPath(self,start,ver):
        if ver==start:
            print(ver)
            
        else:
            self.genPath(start,self.nodes[ver]['pred'])
            print(ver)
            

    def sssp(self,start,end):
        h=[]
        heapq.heappush(h,(0,start))
        while len(h):
            cost,ver=heapq.heappop(h)
            if(ver==end):
                print(f"we can reach from {start} to end {end} with the cost of {cost}")
                path=[]
                self.genPath(start,ver)
                break
            else:
                for c,n in self.graph[ver]:
                    if self.nodes[n]['wt']>(c+cost):
                        self.nodes[n]['wt']=c+cost
                        self.nodes[n]['pred']+=ver
                        heapq.heappush(h,(c+cost,n))
g=Graph()
g.addEdge('A','B',2)
g.addEdge('A','C',5)
g.addEdge('B','C',6)
g.addEdge('B','D',1)
g.addEdge('B','E',3)
g.addEdge('C','F',8)
g.addEdge('D','E',4)
g.addEdge('E','G',9)
g.addEdge('F','G',7)

g.sssp('A',"G")






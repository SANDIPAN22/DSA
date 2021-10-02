from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.edges=[]
        self.nodes=[]

    def addEdge(self,start, end, cost):
        self.graph[start].append((cost,end))
        data={'start':start,'cost':cost,'end':end}
        self.edges.append(data)

        if start not in self.nodes:
            self.nodes.append(start)
        
        if end not in self.nodes:
            self.nodes.append(end)

    
    def findRoot(self,a):
        if self.parent[a]!=a:
            self.parent[a]=self.findRoot(self.parent[a])
        return self.parent[a]
    def union(self,a,b):
        roota=self.findRoot(a)
        rootb=self.findRoot(b)

        if self.rank[roota]<self.rank[rootb]:
            self.parent[roota]=rootb
        if self.rank[roota]>self.rank[rootb]:
            self.parent[rootb]=roota
        else:
            self.parent[rootb]=roota
            self.rank[roota]+=1
    def findMST(self):
        self.parent={}
        self.rank={}
        for i in self.nodes:
            self.parent[i]=i
            self.rank[i]=0
        self.edges.sort(key=lambda a : a['cost'])
        cos=0
            #print(self.findRoot('a'))
        
        for k in self.edges:
            
            ra=self.findRoot(k['start'])
            rb=self.findRoot(k['end'])
            if ra!=rb:
                print(f"Connecting {k['start']} and {k['end']} with cost of {k['cost']}")
                self.union(k['start'],k['end'])
                cos+=k['cost']
                print(f"cost till now ==> {cos}")

g=Graph()
g.addEdge('a','b',5)
g.addEdge('a','c',13)
g.addEdge('a','e',15)
g.addEdge('b','a',5)
g.addEdge('b','c',10)
g.addEdge('b','d',8)
g.addEdge('c','a',13)
g.addEdge('c','b',10)
g.addEdge('c','e',20)
g.addEdge('c','d',6)
g.addEdge('d','b',8)
g.addEdge('d','c',6)
g.addEdge('e','a',15)
g.addEdge('e','c',20)  


g.findMST()


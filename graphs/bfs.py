class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict={}
        else:
            self.gdict=gdict

    def addEdges(self, source, desti):
        self.gdict[source].append(desti)
    def bfs(self, source):
        self.q=[]
        vn=[]
        self.q.append(source)
        while len(self.q):
            p=self.q.pop(0)
            
            for v in self.gdict[p]:
                if v not in vn:
                    self.q.append(v)
            if p not in vn:
                print(p)
                vn.append(p)
        
            

g={'a':['b','c','d'],
    'b':['a','e'],
    'c':['a','d'],
    'd':['c','a','e'],
    'e':['b','d']

        }

grph=Graph(g)
grph.addEdges('b','d')
print(grph.gdict)
grph.bfs('a')
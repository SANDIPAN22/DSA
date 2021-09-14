class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict={}
        else:
            self.gdict=gdict

    def addEdges(self, source, desti):
        self.gdict[source].append(desti)

g={'a':['b','c','d'],
    'b':['a','e'],
    'c':['a','d'],
    'd':['c','a','e'],
    'e':['b','d']

        }

grph=Graph(g)
grph.addEdges('b','d')
print(grph.gdict)

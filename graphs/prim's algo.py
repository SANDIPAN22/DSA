import sys
inf=sys.maxsize

class Graph:
    def __init__(self,edges,nodes):
        self.e=edges
        self.nodes=nodes
        self.visited=[]
        self.data={}
        for i in self.nodes:
            d={'cost':inf,'parent':''}
            self.data[i]=d
        self.data[self.nodes[0]]['cost']=0
    def primsMST(self):
        # for i in range(len(self.nodes)):
        mst={}
        
        i=0
        while len(self.visited)<len(self.nodes):
            
            for j in range(len(self.nodes)):
                
                if self.nodes[j] not in self.visited:
                    if i!=j and self.e[i][j]!=inf:
                        
                        self.data[self.nodes[j]]['cost']=min(self.data[self.nodes[j]]['cost'],self.e[i][j])
                        self.data[self.nodes[j]]['parent']=self.nodes[i]
            self.visited.append(self.nodes[i])
            
            mst[self.nodes[i]]=(self.data.pop(self.nodes[i]))
            if len(self.data):
                i=(self.nodes.index(sorted(list(self.data.items()),key=lambda a: a[1]['cost'])[0][0]))
        return mst
            #print( list(self.data.items()))
            
            

e=[[0,10,20,inf,inf],
    [10,0,30,5,inf],
    [20,30,0,15,6],
    [inf,5,15,0,inf],
    [inf,inf,6,8,0]]
nodes=['a','b','c','d','e']
g=Graph(e,nodes)
print(g.primsMST())

class DisjointSet:
    def __init__(self):
        self.parent={}
        self.rank={}
    def makeSet(self,nodes):
        for k in nodes:
            self.parent[k]=k
            self.rank[k]=0
    def find(self,a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def union(self,a,b):
        roota=self.find(a)
        rootb=self.find(b)

        if self.rank[roota]>self.rank[rootb]:
            self.parent[rootb]=roota
        elif self.rank[roota]<self.rank[rootb]:
            self.parent[a]=rootb
        else:
            self.rank[roota]+=1
            self.parent[rootb]=roota

    def printSet(self,nodes):
        print([self.find(i) for i in nodes])

d=DisjointSet()
n=[1,2,3,4,5]
d.makeSet(n)
d.printSet(n)
d.union(4,3)
d.printSet(n)
d.union(2,1)
d.printSet(n)
d.union(1,3)
d.printSet(n)
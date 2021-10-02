class Tree:
    def __init__(self,data,child=[]):
        self.data=data
        self.children=child
    def addChild(self,node):
        self.children.append(node)
    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for c in self.children:
            ret+=c.__str__(level+1)
        return ret

menu=Tree('menu',[])
hd=Tree('Hard Drinks',[])
sd=Tree('Soft Drinks',[])
menu.addChild(hd)
menu.addChild(sd)
wine=Tree('Wine',[])
beer=Tree('Beer',[])
hd.addChild(wine)
hd.addChild(beer)

coke=Tree('Coke',[])
ms=Tree('Milk Shake',[])
sd.addChild(coke)
sd.addChild(ms)


print(menu)
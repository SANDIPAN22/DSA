class TreeNode:
    def __init__(self,size):
        self.size=size
        self.tree=[None]*size
        self.lastUsedIndex=0

    def addElement(self,element):
        if self.lastUsedIndex+1==self.size:
            print('oops no place to enter')
        else:
            self.tree[self.lastUsedIndex+1]=element
            self.lastUsedIndex+=1
            print('element has been entered successfully!!')

    def preorder(self,index):
        if index>self.lastUsedIndex:
            return
        else:
            print(self.tree[index])
            self.preorder(index*2)
            self.preorder(index*2+1)

    def inorder(self,index):
        if index>self.lastUsedIndex:
            return
        else:
            self.inorder(index*2)
            print(self.tree[index])
            self.inorder(index*2+1)

    def postorder(self,index):
        if index>self.lastUsedIndex:
            return
        else:
            self.postorder(index*2)
            self.postorder(index*2+1)
            print(self.tree[index])

    def levelorder(self):
        for k in self.tree[1:]:
            if k:
                print(k)
            else:
                return

    def deleteNode(self,element):
        if self.lastUsedIndex==0:
            print("Nothing is here to delete")
        else:
            if element in self.tree:
                i=self.tree.index(element)
                self.tree[i]=self.tree[self.lastUsedIndex]
                self.tree[self.lastUsedIndex]=None
                self.lastUsedIndex-=1

    def deleteTree(self):
        self.tree=None

    def srch(self,element):
        if self.lastUsedIndex==0:
            print("Nothing is here to delete")
        else:
            if element in self.tree:
                i=self.tree.index(element)
                print(i)
            else:
                print('cannot find the element')


nbt=TreeNode(8)
nbt.addElement('drinks')
nbt.addElement('hot')
nbt.addElement('cold')
nbt.addElement('tea')
nbt.addElement('coffee')

nbt.levelorder()
nbt.deleteNode('tea')
print()
nbt.levelorder()
nbt.deleteTree()



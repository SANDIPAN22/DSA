class TreeNode: 
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addLeftChild(self,node):
        self.left=node
    def addRightChild(self,node):
        self.right=node
def preorder(node):
    if node==None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)
    
def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
def levelorder(node):
        
    q=[]
    q.append(node)
    while len(q):
        v=q.pop(0)
        if  v.left:
            q.append(v.left)
        if  v.right:
            q.append(v.right)
        print(v.data)
def srch(rt,node):
    q=[]
    q.append(rt)
    while len(q):
        v=q.pop(0)
        
        if v.data==node:
            print("got it")
            return
        if  v.left:
            q.append(v.left)
        if  v.right:
            q.append(v.right)

    print('sorry not available !!')


def insertNode(rt,node):
    #enter wherever we get a blank
    q=[]
    q.append(rt)
    while len(q):
        n=q.pop(0)
        if n.left:
            q.append(n.left)
        elif not n.left:
            n.left=(node)
            print("element entered")
            return
        elif n.right:
            q.append(n.right)
        elif not n.right:
            n.right=node
            print('element entered')
            return
def setTree(node,dir,val=None):
    if dir=='':
        print("deleting tree",node.data)
        node.data=None
        node.left=None
        node.right=None
        return
    if val:
        if dir=='l':
            node.left.data=val
        else:
            node.right.data=val
    else:
        if dir=='l':
            node.left=val
        else:
            node.right=val

def dltUtil(tr,d):
    q=[]
    
    bap=tr
    lr=''
    q.append((bap,lr,tr))
    db=tr
    dlr=''

    while len(q):
        bap,lr,node=q.pop(0)
        if node.data==d:
           
            db=bap
            dlr=lr

        if node.left:
            q.append((node,'l',node.left))
        if node.right:
            q.append((node,'r',node.right))
    setTree(bap,lr)
    setTree(db,dlr,node.data)


drink=TreeNode('drink')
soft=TreeNode('soft')
hard=TreeNode('hard')
coke=TreeNode('coke')
shake=TreeNode('shake')
wine=TreeNode('wine')
beer=TreeNode('beer')
drink.addLeftChild(soft)
drink.addRightChild(hard)
soft.addLeftChild(coke)
soft.addRightChild(shake)
hard.addRightChild(beer)
hard.addLeftChild(wine) 
gc=TreeNode('gola cola')
# preorder(drink)
# levelorder(drink)
srch(drink,'ber')
insertNode(drink,gc)
levelorder(drink)
dltUtil(drink,'drink')
print()
levelorder(drink)
print()
levelorder(drink)
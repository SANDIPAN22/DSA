class AVLnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

def getHeight(root):
    if not root:
        return 0
    else:
        return root.height

def leftRotation(ubroot):
    newNode=ubroot.right
    ubroot.right=newNode.left
    # newNode.left=None
    newNode.left=ubroot
    newNode.height=1+max(getHeight(newNode.left),getHeight(newNode.right))
    ubroot.height=1+max(getHeight(ubroot.left),getHeight(ubroot.right))
    return newNode

def rightRotation(ubroot):
    newNode=ubroot.left
    ubroot.left=newNode.right
    # newNode.right=None
    newNode.right=ubroot
    newNode.height=1+max(getHeight(newNode.left),getHeight(newNode.right))
    ubroot.height=1+max(getHeight(ubroot.left),getHeight(ubroot.right))
    return newNode

def getBalance(root):
    if not root: 
        return 0
    else:
        return getHeight(root.left)-getHeight(root.right)

def insertNode(root,value):
    if not root:
        return AVLnode(value)
    else:
        if value<=root.data:
            root.left=insertNode(root.left,value)
        elif value>root.data:
            root.right=insertNode(root.right,value)
    
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    bal=getBalance(root)
    if bal>1 and value<root.left.data:
        ## LL==> right rotation
        return rightRotation(root)
    elif bal>1 and value>root.left.data:
        # LR==> Left(root.left)  right(root)
        root.left=leftRotation(root.left)
        return rightRotation(root)
    elif bal<-1 and value>root.right.data:
        # RR==> Left rotation
        return leftRotation(root)
    elif bal<-1 and value<root.right.data:
        # RL ==> right(root.right)  left(root)
        root.right=rightRotation(root.right)
        return leftRotation(root)
    return root

def preorder(root):
    if not root:
        return
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorderSuccessor(root):
    current=root
    while current.left!=None:
        current=current.left
    return current
def deleteNode(root,val):
    if not root:
        return root
    elif val<root.data:
        root.left=deleteNode(root.left,val)
    elif val>root.data:
        root.right=deleteNode(root.right,val)
    else:
        if not root.left:
            temp=root.right
            root=None
            return temp
        elif not root.right:
            temp=root.left
            root=None
            return temp
        else:
            temp=inorderSuccessor(root.right)
            root.data=temp.data
            root.right=deleteNode(root.right,temp.data)
        bal=getBalance(root)
        if bal>1 and getBalance(root.left)>=0:
            #LL==> right rotation(root)
            return rightRotation(root)
        elif bal>1 and getBalance(root.left)<0:
            #LR ==> Left rotation(root.lrft) -> right rotation(root)
            root.left=leftRotation(root.left)
            return rightRotation(root)
        elif bal<-1 and getBalance(root.right)>0:
            #RL ==> Right rotation(root.right) -> left rotation(root)
            root.right=rightRotation(root.right)
            return leftRotation(root)
        elif bal<-1 and getBalance(root.right)<=0:
            #RR ==> left rotation
            return leftRotation(root)
    return root


root = None
 
root = insertNode(root, 10)
root = insertNode(root, 20)
root = insertNode(root, 30)
root = insertNode(root, 40)
root = insertNode(root, 50)
root = insertNode(root, 25)

preorder(root)
print()
root=deleteNode(root,170)

preorder(root)


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def addNode(node,value):
    if node==None:
        return TreeNode(value)
    elif value<=node.data:
        node.left=addNode(node.left,value)
    elif value>node.data:
        node.right=addNode(node.right,value)
    return node

def inorder(root):
    if root==None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def search(root,val):
    if root == None:
        print('Unable to find it !!')
    elif root.data==val:
        print('got it !!')
        
    elif root.data>val:
        search(root.left,val)
    elif root.data<val:
        search(root.right,val)

def inorderSuccessor(root):
    current=root
    while current.left!=None:
        current=current.left
    return current
def dl8Util(root,val):
    if root==None:
        return root
    elif val<root.data:
        root.left=dl8Util(root.left,val)
    elif val>root.data:
        root.right=dl8Util(root.right,val)
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
            root.right=dl8Util(root.right,temp.data)
    return root

    


root=None
root=addNode(root,10)

root=addNode(root,2)

root=addNode(root,15)
root=addNode(root,1)
root=addNode(root,20)
root=addNode(root,26)
root=addNode(root,5)
root=addNode(root,6)


inorder(root)
search(root,20)

dl8Util(root,2)
print()
inorder(root)

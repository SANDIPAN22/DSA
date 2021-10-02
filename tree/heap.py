class Heap:
    def __init__(self,size,htype):
        self.heap=[None]*(size+1)
        self.lastUsedIndex=0
        self.size=(size+1)
        self.htype=htype
def peak(root):
    if root.lastUsedIndex==0:
        print("nothing in the heap")
    else:
        print(root.heap[1])
def preorder(root,index):
    if index>root.lastUsedIndex:
        return 
    else:
        print(root.heap[index])
        preorder(root,index*2)
        preorder(root,index*2+1)
def heapifyInsert(root,index):
    if index<=1:
        return
    parentIndex=int(index/2)
    if root.htype=='min':

        if root.heap[index]<root.heap[parentIndex]:
            root.heap[index],root.heap[parentIndex]=root.heap[parentIndex],root.heap[index]
        heapifyInsert(root,parentIndex)
    else:
        if root.heap[index]>root.heap[parentIndex]:
            root.heap[index],root.heap[parentIndex]=root.heap[parentIndex],root.heap[index]
        heapifyInsert(root,parentIndex)
def insertNode(root,value):
    if root.lastUsedIndex+1 == root.size:
        print("Nomore place to enter")
        return None
    else:
        root.heap[root.lastUsedIndex+1]=value
        root.lastUsedIndex+=1
        heapifyInsert(root,root.lastUsedIndex)
        return root
def heapifyExtract(root,index):
    left=index*2
    right=index*2+1
    if left>root.lastUsedIndex:
        return
    elif left==root.lastUsedIndex:
        if root.htype=='min':
            if root.heap[index]>root.heap[left]:
                root.heap[index],root.heap[left]=root.heap[left],root.heap[index]
                return
        else:
            if root.heap[index]<root.heap[left]:
                root.heap[index],root.heap[left]=root.heap[left],root.heap[index]
                return
    else:
        
        if root.htype=='min':
            if root.heap[left]<root.heap[right]:
                minChild=left
            else:
                minChild=right
            if root.heap[index]>root.heap[minChild]:
                root.heap[index],root.heap[minChild]=root.heap[minChild],root.heap[index]
            heapifyExtract(root,minChild)
        else:
            if root.heap[left]>root.heap[right]:
                maxChild=left
            else:
                maxChild=right
            if root.heap[index]<root.heap[maxChild]:
                root.heap[index],root.heap[maxChild]=root.heap[maxChild],root.heap[index]
            heapifyExtract(root,maxChild)


def extract(root):
    if root.lastUsedIndex==0:
        print('nothing to extract')
        return
    else:
        d=root.heap[1]
        root.heap[1],root.heap[root.lastUsedIndex]=root.heap[root.lastUsedIndex],root.heap[1]
        root.heap[root.lastUsedIndex]=None
        root.lastUsedIndex-=1
        heapifyExtract(root,1)
        return d

root=Heap(10,'min')
root=insertNode(root,10)
root=insertNode(root,50)
root=insertNode(root,90)
root=insertNode(root,100)
root=insertNode(root,15)
root=insertNode(root,18)

# preorder(root,1)
print(extract(root))
print()

preorder(root,1)

print()
peak(root)
def dl8(hashTable,b):
    hv=hasing(len(hashTable),b)
    if b in hashTable[hv]:
        hashTable[hv].remove(b)
        print("deleted")
    else:
        print("not in the hash table")

def find(hashTable,a):
    hv=hasing(len(hashTable),a)
    if a in hashTable[hv]:
        print(f" {hv}==>{hashTable[hv].index(a)}")
    else:
        print("not in the hash table")
def hasing(size,n):
    return n%size
def insertElement(hashTable,n):
    hv=hasing(len(hashTable),n)
    hashTable[hv].append(n)

hashTable=[[] for i in range(10)]
insertElement(hashTable,5)
insertElement(hashTable,15)
insertElement(hashTable,2)
insertElement(hashTable,8)

find(hashTable,15)


print(hashTable)

dl8(hashTable,15)


print(hashTable)
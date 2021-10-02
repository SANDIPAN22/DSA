class Tries:
    def __init__(self):
        self.dic={}
        self.eos='N'

def addString(root,value):
    for k in value:
        if len(root.dic.keys())==0 or k not in list(root.dic.keys()):
            # we can write the above condition as=> if not root.dic.get(k):
            root.dic[k]=Tries()
        root=root.dic[k]
    root.eos='Y'

def searchString(root,value):
    for k in value:
        if not root.dic.get(k):
            print('Not available !!')
            return
        else:
            root=root.dic.get(k)
    if root.eos=='Y':
        print('Yesss!! we got it!')
    else:
        print('Not available !!')

def deleteStr(root,word,ind):
    ch=word[ind]
    node=root.dic.get(ch)
    dl=False

    if len(node.dic)>1:
        deleteStr(node,word,ind+1)
        return False
    if ind == len(word)-1:
        if len(node.dic)>=1:
            node.eos='N'
            return False
        else:
            root.dic.pop(ch)
            return True
    if node.eos=='Y':
        deleteStr(node,word,ind+1)
        return False

    dl=deleteStr(node,word,ind+1)
    if dl:
        root.dic.pop(ch)
        return True
    else:
        return False


root=Tries()
addString(root,'a')
addString(root,'app')
addString(root,'apple')
addString(root,'api')
addString(root,'apis')

deleteStr(root,'api',0)

searchString(root,'api')

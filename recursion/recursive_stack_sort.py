def stackSort(s):
    if len(s)!=0:
        temp=s.pop()
        stackSort(s)
        sortedPush(s,temp)

def sortedPush(s,temp):
    if len(s)==0 or temp<s[-1]:
        s.append(temp)
    else:
        element=s.pop()
        sortedPush(s,temp)
        s.append(element)

s=[10,56,8,10,6]
stackSort(s)
print(s)



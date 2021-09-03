def rev_stack(s):
    if len(s)!=0:
        temp=s.pop()
        rev_stack(s)
        # print(temp)
        insertBottom(s,temp)
def insertBottom(s,temp):
    if len(s)==0:
        s.append(temp)
    else:
        element=s.pop()
        insertBottom(s,temp)
        s.append(element)
s=[10,20,60,88]
rev_stack(s)
print(s)
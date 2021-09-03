s=[1,5,6,8,7]
k=(len(s)//2)+1

def dl8MidElement(s):
    if len(s)!=0:
        t=s.pop()
        dl8MidElement(s)
        global k
        
        if len(s)!=k-1:
            s.append(t)
        else:
            k=-1
            
           

dl8MidElement(s)
print(s)



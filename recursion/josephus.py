def josephus(n,k,v,i):
    if n==1:
        print(v[0])
        return
    else:
        i=(i+k)%n
        v.pop(i)
        josephus(n-1,k,v,i+1)

josephus(5,2-1,["A","B","C","D","E"],0)

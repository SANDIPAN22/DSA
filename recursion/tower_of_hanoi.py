def toh(n,source,desti,aux):
    if n==1:
        print(f"the {n}th disk moved from {source} to {desti}")
        return
    else:
        toh(n-1,source,aux,desti)
        print(f"the {n}th disk moved from {source} to {desti}")
        toh(n-1,aux,desti,source)

n=3
toh(n,'A','C','B')
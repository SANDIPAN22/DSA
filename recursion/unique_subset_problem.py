arr=[]
def uniq_subset_prob(ip,op):
    if len(ip)==0:
        arr.append(op)
        return 
    else:
        op1=op
        op2=op
        op2+=ip[0]
        ip=ip[1:]
        uniq_subset_prob(ip,op1)
        uniq_subset_prob(ip,op2)

uniq_subset_prob('aab','')
arr2=[]
for k in arr:
    if k  not in arr2:
        arr2.append(k)
print(*arr2)
    
def subsetProb(ip,op):
    if len(ip)==0:
        print(f"'{op}'")
        return 
    else:
        op1=op
        op2=op
        op2+=ip[0]
        ip=ip[1:]
        
        subsetProb(ip,op1)
        subsetProb(ip,op2)

subsetProb("abc",'')
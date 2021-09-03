# def permu_space(ip,op):
#     if len(ip)==1:
#         print(op)
#         return
#     else:
#         op1=op
#         op2=op
#         op2=op[:op.index(ip[0])+1]+'_'+op[op.index(ip[0])+1:]
#         ip=ip[1:]
#         permu_space(ip,op1)
#         permu_space(ip,op2)

def permu_space(ip,op):
    if len(ip)==0:
        print(op)
        return
    else:
        op1=op
        op2=op
        op1+=ip[0]
        op2+='_'+ip[0]
        ip=ip[1:]
        permu_space(ip,op1)
        permu_space(ip,op2)


ip="ABCAD"
permu_space(ip[1:],ip[0])
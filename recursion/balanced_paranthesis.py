def balanced_paran(ob,cb,op):
    
    if(ob==0 and cb==0):
        print(op)
        return 
    else:
        if ob<cb:
            if ob==0:
                opp=op+')'
                cb-=1
                balanced_paran(ob,cb,opp)
            else:
                op1=op+'('
                ob1=ob
                ob1-=1
                op2=op+')'
                cb2=cb
                cb2-=1
                balanced_paran(ob1,cb,op1)
                balanced_paran(ob,cb2,op2)
        else:
            op=op+'('
            ob-=1
            balanced_paran(ob,cb,op)

balanced_paran(2,2,'')

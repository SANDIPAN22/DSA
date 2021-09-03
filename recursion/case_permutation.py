def case_permu(ip,op):
    numb=['1','2','3','4','5','6','7','8','9','0']
    if len(ip)==0:
        print(op)
        return 
    else:
        if ip[0] not in numb:
            op1=op+ip[0].lower()  
            op2=op+ip[0].upper()
            ip=ip[1:]
            case_permu(ip,op1)
            case_permu(ip,op2) 
        else:
            opp=op+ip[0]  
            ip=ip[1:]
            case_permu(ip,opp)

        

case_permu('A5B79','')
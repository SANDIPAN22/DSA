def find(n,zeros,ones,op):
    if n==0:
        print(op)
        return 
    else:
        if zeros<ones:
            find(n-1,zeros+1,ones,op+'0')
            find(n-1,zeros,ones+1,op+'1')
        else:
            find(n-1,zeros,ones+1,op+'1')

find(4,0,0,'')

# result
# 1111
# 1110
# 1101
# 1100
# 1011
# 1010
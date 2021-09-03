def solve(n,k):
    if n==1 and k==1:
        return 0
    else:
        if k%2==0:
            return 1-(solve(n-1,k//2))
        else:
            return solve(n-1,(k+1)//2)

print(solve(4,8))

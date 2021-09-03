
def decimal2binary(n):
    if n==0:
        return 0
    else:
        
        return 10*(decimal2binary(n//2))+n%2

print(decimal2binary(12))

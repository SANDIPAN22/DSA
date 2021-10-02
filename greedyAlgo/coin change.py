## MINIMUM NUMBER COIN TO FULL FILL THE TOTAL VALUE

def coinChange(coins,value):
    coins.sort(reverse=True)
    while value:
        for j in coins:
            if value>=j:
                print(j)
                value-=j
                break

coins=[1,2,5,20,50,100]
coinChange(coins,201)
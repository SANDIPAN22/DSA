class Product:
    def __init__(self,wt,tc):
        self.wt=wt
        self.tc=tc
        self.ratio=tc/wt

class Knapsack:
    def __init__(self,capacity):
        self.capacity=capacity

def maximumProfit(productList,knapsack):
    productList.sort(key= lambda h: h.ratio, reverse=True)
    value=0
    for p in productList:
        if knapsack.capacity==0:
            break
        if p.wt<=knapsack.capacity:
            knapsack.capacity-=p.wt
            print(p.wt)
            value+=p.tc
            print("remaining weight ",knapsack.capacity)
        else:
            
            print(knapsack.capacity)
            value+=knapsack.capacity*(p.ratio)
    print()
    print(value)

prod1=Product(20,100)
prod2=Product(30,120)
prod3=Product(10,60)
plist=[prod1,prod2,prod3]

k1=Knapsack(50)

maximumProfit(plist,k1)




    
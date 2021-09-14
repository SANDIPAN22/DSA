def arrSrt(arr,n):
    for i in range (1,n):
        j=i-1
        s=i
        while (j>=0 and arr[j]>arr[s]):
            
            arr[s],arr[j]=arr[j],arr[s]
            j-=1
            s-=1

arr=[12,8,56,4,2,99,1]
arrSrt(arr,7)
print(arr)
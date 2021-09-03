# def insertionSort(arr,n):
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while(j>=0 and arr[j]>key):
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key

def RecursiveInsertionSort(arr,n):
    if n<=1:
        return 
    RecursiveInsertionSort(arr,n-1)
    key=arr[n-1]
    j=n-2
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

arr=[12,89,8,6,2,15]
RecursiveInsertionSort(arr,len(arr))
print(arr)
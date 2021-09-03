# def b_sort(arr,n):
#     for i in range(0,n-1):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

def b_sort(arr,n):
    if n<=1:
        return
    b_sort(arr,n-1)
    for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    


arr=[45,89,1,6,78]
b_sort(arr,len(arr))
print(arr)
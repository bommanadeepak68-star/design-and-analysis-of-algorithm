arr = [-12,19,-9,0,4,8]
n = len(arr)
for i in range(n-1):
    for j in range(n-1-i):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)            
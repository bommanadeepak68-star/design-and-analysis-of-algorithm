arr = [7,9,3,6,2,-1,0]
n = len(arr)
for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>= 0 and arr[j]>key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1]= key
print(arr)
def linearsearch(arr,n,key):
    for i in range (n):
        if arr[i]==key:
            return i
    return-1
n = int(input("enter the size of array:"))
arr = []
for i in range(n):
    value = int(input(f"enter the array{i+1}:"))
    arr.append(value)
n = len(arr)
key = int(input("enter the number:"))
ans = linearsearch(arr,n,key)
print("array at index no :",ans)

    
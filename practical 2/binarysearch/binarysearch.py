
def binarysearch(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]== key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return -1
n = int(input("enter the size of array:"))
arr = []
for i in range(n):
    value = int(input(f"enter the array {i+1}:"))
    arr.append(value)

key = int(input("enter the number:"))
ans = binarysearch(arr,key)

if ans !=-1:
    print(f"your number found at index {ans}")
else:
    print("not found")


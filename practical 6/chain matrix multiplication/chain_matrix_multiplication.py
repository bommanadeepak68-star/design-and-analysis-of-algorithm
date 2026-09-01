def matrix_chain_multiplication(arr):
    n = len(arr)-1

    dp =[[0 for i in range(n)] for i in range(n)]

    for length in range(2,n+1):
        
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i,j):

                cost = (
                    dp[i][k]+dp[k+1][j]+arr[i]*arr[k+1]*arr[j+1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n-1]

arr = []
n = int(input("enter the number of matrices:"))
for i in range(n+1):
    x = int(input(f"enter the dimensions{i+1}:"))
    arr.append(x)
result = matrix_chain_multiplication(arr)
print("minimum number of multiplications:",result)
        
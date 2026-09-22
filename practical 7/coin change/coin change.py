def coin_change(N,coins):
    n = len(coins)
    dp =[[0 for j in range(N+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,N+1):
            if coins[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
    return dp[n][N]

coins = []
N = int(input("enter the amount:"))
n = int(input("enter the number of coins:"))
for i in range(n+1):
    x = int(input(f"enter the coins{i+1}:"))
    coins.append(x)
result = coin_change(N,coins)
print("minimum number of ways:",result)


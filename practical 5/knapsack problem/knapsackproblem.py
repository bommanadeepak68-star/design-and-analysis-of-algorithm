n = int(input("enter the number of items:"))

weights = []
values = []


for i in range(n):
    a = int(input(f"enter the weight of item{i+1}:"))
    weights.append(a)

    b = int(input(f"enter the values of items{i+1}:"))
    values.append(b)

capacity = int(input("enter the capacity of knapsack:"))

dp = [[0 for i in range(capacity + 1)] for i in range(n+1)]

for i in range(1,n+1):
    for w in range(1,capacity+1):

        if weights[i-1]<=w:
            dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
print("maximum value = ",dp[n][capacity])
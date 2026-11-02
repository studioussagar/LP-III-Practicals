
n = int(input("Enter number of items: "))

profits = []
weights = []

# Accept profit and weight of each item
for i in range(n):
    profit = int(input("Enter profit: "))
    weight = int(input("Enter weight: "))

    profits.append(profit)
    weights.append(weight)

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum profit
print("\nMaximum Profit:", dp[n][capacity])
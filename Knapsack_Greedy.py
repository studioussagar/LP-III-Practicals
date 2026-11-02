n = int(input("Enter number of items: "))

items = []

# Accept profit and weight
for i in range(n):
    profit = int(input("Enter profit: "))
    weight = int(input("Enter weight: "))

    ratio = profit / weight
    items.append((profit, weight, ratio))

capacity = int(input("Enter knapsack capacity: "))

# Sort by profit/weight ratio
items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

# Select items using Greedy Method
for profit, weight, ratio in items:
    if capacity >= weight:
        total_profit += profit
        capacity -= weight
    else:
        total_profit += ratio * capacity
        break

# Display maximum profit
print("\nMaximum Profit:", round(total_profit, 2))
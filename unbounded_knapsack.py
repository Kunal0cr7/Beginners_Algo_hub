def unbounded_knapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example usage:
values = [10, 30, 20]
weights = [5, 10, 15]
capacity = 100

max_value = unbounded_knapsack(values, weights, capacity)
print("Maximum value:", max_value)

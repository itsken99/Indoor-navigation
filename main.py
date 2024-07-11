def knapsack(W, weights, values, n):
    # Initialize DP table with all zeros
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # K[n][W] contains the maximum value that can be attained with the given capacity
    return K[n][W]

# Example parameters
W = 50
weights = [10, 20, 30]
values = [60, 100, 120]
n = len(weights)

# Solve the problem
max_value = knapsack(W, weights, values, n)
print(f"The maximum value that can be put in a knapsack of capacity {W} is {max_value}")

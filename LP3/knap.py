n = int(input("Enter number of items: "))
capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0:
    print("Invalid input")

else:
    weights = list(map(int, input("Enter weights: ").split()))
    values = list(map(int, input("Enter values: ").split()))

    # Create DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # Do not include current item
            dp[i][w] = dp[i - 1][w]

            # Include current item if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    print("Maximum value:", dp[n][capacity])
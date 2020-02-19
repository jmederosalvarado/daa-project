def arranging_heaps(weights, k):
    n = len(weights)

    w = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            w[i, j] = weights[i](j-i)

    dp = [[0]*n for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(n):
            dp[i][j] = 1e5  # some big value here
            for k in range(j):
                dp[i][j] = min(dp[i][j], dp[i-1][k] + w[k+1][j])

    return dp[k][n-1]

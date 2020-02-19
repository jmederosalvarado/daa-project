def optimal_bst(frequencies):
    n = len(frequencies)

    w = [[0]*n for _ in range(n)]
    for i in range(n):
        w[i][i] = frequencies[i]
    for i in range(n):
        for j in range(i+1, n):
            w[i, j] = w[i, j-1] + frequencies[j]

    dp = [[0]*n for _ in range(n)]
    for l in range(1, n):
        for i in range(n-l):
            j = i + l
            dp[i][j] = 1e5  # some big value here
            for k in range(i+1, j-1):
                dp[i][j] = w[i][j] + min(dp[i][j], dp[i][k-1] + dp[k][j])

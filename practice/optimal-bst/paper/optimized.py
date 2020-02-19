def optimal_bst(frequencies):
    n = len(frequencies)

    w = [[0]*n for _ in range(n)]
    for i in range(n):
        w[i][i] = frequencies[i]
    for i in range(n):
        for j in range(i+1, n):
            w[i, j] = w[i, j-1] + frequencies[j]

    mids = [[0]*n for _ in range(n)]
    for i in range(n):
        mids[i][i] = i

    dp = [[0]*n for _ in range(n)]
    for l in range(1, n):
        for i in range(n-l):
            j = i + l

            dp[i][j] = 1e5  # some big value here
            mleft, mright = mids[i][j-1], mids[i+1][j]
            for k in reversed(range(mleft, mright+1)):
                current = w[i][j] + min(dp[i][j], dp[i][k-1] + dp[k][j])
                if dp[i][j] > current:
                    dp[i][j], mids[i][j] = current, k

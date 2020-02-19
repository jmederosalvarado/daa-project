from optimization import compute_dp


def arranging_heaps(weights, k):
    n = len(weights)

    w = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            w[i, j] = weights[i](j-i)

    dp = [[0]*n for _ in range(k+1)]
    compute_dp(dp, w, i, 0, n, 1, k+1)

    return dp[k][n-1]

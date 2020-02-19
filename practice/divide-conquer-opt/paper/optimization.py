def compute_dp(dp, w, i, jleft, jright, kleft, kright):
    jmid = (jleft + jright) / 2  # middle point

    # compute value of dp[i][jmid] by definition of dp
    dp[i][jmid] = 1e5  # some large value here
    bestk = -1
    for k in range(kleft, jmid):
        current = dp[i - 1][k] + w[k + 1][jmid]
        if current < dp[i][jmid]:
            dp[i][jmid] = current
            bestk = k

    # divide and conquer
    if jleft < jmid - 1:
        compute_dp(dp, w, i, jleft, jmid - 1, kleft, bestk)
    if jleft + 1 < jright:
        compute_dp(dp, w, i, jmid + 1, jright, bestk, kright)

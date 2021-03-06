from itertools import combinations


def mask(i, n):
    """Returns a number where the bit n-i-1 is on"""
    return 1 << (n-i-1)


def outdegree(n, v, edges, taken):
    return sum((1 for i in range(n) if (mask(i, n) & (edges & taken))))


def greedy(n, adj):
    dominants, taken = [], 0

    while True:
        v = max((i for i in range(n)
                 if not (mask(i, n) & taken)),
                key=lambda i: outdegree(n, i, adj[i], taken),
                default=None)

        if v is None:
            break

        dominants.append(v)
        taken |= mask(v, n) | adj[v]

    return dominants


def is_dominating(n, s, adj):
    taken = 0
    for i in s:
        taken |= (1 << n-i-1) | adj[i]
    return taken == (1 << n) - 1


def search_all(n, k, adj):
    for i in range(1, k):
        for dom in combinations(range(n), i):
            if is_dominating(n, dom, adj):
                return dom


def infiltrations(n, adj):
    greedy_ans = greedy(n, adj)
    improved = search_all(n, len(greedy_ans), adj)
    return improved or greedy_ans

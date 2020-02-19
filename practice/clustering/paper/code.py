from disjoint_sets import DisjointSets


def clustering(n, k, edges):
    clusters = DisjointSets(n)

    edges = sorted(edges, lambda e: e[0])
    for _, u, v in edges:
        if clusters.merge(u, v):
            cc -= 1
        if clusters.count == k:
            break

    return clusters.parents

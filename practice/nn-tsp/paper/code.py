def nn_tsp(weights):
    n = len(weights)

    tour, visited = [0], [False]*n
    for v in range(n):
        nn, nn_cost = -1, 1e5
        if tour[-1] != v and not visited[v]:
            if nn_cost > weights[tour[-1], v]:
                nn, nn_cost = v, weights[tour[-1], v]
        visited[nn] = True
        tour.append(nn)

    return tour

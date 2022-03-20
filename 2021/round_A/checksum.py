T = int(input())
for t in range(T):
    N = int(input())
    A = []
    for n in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for n in range(N):
        B.append(list(map(int, input().split())))
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))

    graph = {}
    for r in range(N):
        for c in range(N):
            if A[r][c] == -1:
                r_label = f"r{r}"
                c_label = f"c{c}"
                if r_label not in graph:
                    graph[r_label] = {}
                if c_label not in graph:
                    graph[c_label] = {}
                graph[r_label][c_label] = B[r][c]
                graph[c_label][r_label] = B[r][c]

    # https://en.wikipedia.org/wiki/Prim%27s_algorithm
    C_v = {v: 0 for v in graph.keys()}
    E_v = {v: None for v in graph.keys()}
    F = {}
    Q = list(graph.keys())
    while len(Q) > 0:
        max_C = None
        max_v = None
        for v in Q:
            if max_C is None or max_C < C_v[v]:
                max_C = C_v[v]
                max_v = v
        Q.remove(max_v)
        F[max_v] = {}
        if E_v[max_v]:
            F[max_v][E_v[max_v][0]] = E_v[max_v][1]  # type: ignore
        for w, c in graph[max_v].items():
            if w in Q and c > C_v[w]:
                C_v[w] = c
                E_v[w] = (max_v, c)  # type: ignore

    weight_sum = 0
    for w in graph.values():
        for c in w.values():
            weight_sum += c
    weight_sum = weight_sum // 2
    result = 0
    for w in F.values():
        for c in w.values():
            result += c
    print(f"Case #{t + 1}: {weight_sum - result}")

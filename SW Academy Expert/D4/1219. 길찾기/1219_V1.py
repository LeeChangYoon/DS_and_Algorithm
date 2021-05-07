def dfs(n):
    global ans

    if n == 99:
        ans = 1

    else:
        if n in node:
            for i in node[n]:
                dfs(i)


for _ in range(10):  # 나중에 10으로 고쳐줘야 함
    T, N = map(int, input().split())
    vertex = [int(i) for i in input().strip().split()]
    node = {}
    ans = 0

    for i in range(N):
        if vertex[2 * i] not in node:
            node[vertex[2 * i]] = [vertex[2 * i + 1]]
        else:
            node[vertex[2 * i]].append(vertex[2 * i + 1])

    dfs(0)
    print("#{} {}".format(T, ans))
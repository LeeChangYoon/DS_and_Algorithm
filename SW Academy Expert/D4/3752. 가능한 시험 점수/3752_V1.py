def dfs(root, idx):
    if idx == N:
        if root in visit:
            return
        else:
            visit[root] = 1
            return

    else:
        # print("{} {}".format(root, idx))

        dfs(root, idx + 1)
        dfs(root + test[idx], idx + 1)


visit = {}

for T in range(1, int(input()) + 1):
    N = int(input())
    test = [int(i) for i in input().strip().split()]

    dfs(0, 0)
    print("#{} {}".format(T, len(visit)))


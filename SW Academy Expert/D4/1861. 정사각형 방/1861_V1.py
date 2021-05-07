def dfs(map1, x, y, cnt, target):
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < N and 0 <= ty < N and map1[x][y] + 1 == map1[tx][ty]:
            cnt += 1
            return dfs(map1, tx, ty, cnt, target)

    else:
        ans.append((target, cnt))


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


for T in range(1, int(input()) + 1):
    ans = []
    N = int(input())
    map1 = [[int(i) for i in input().strip().split()] for _ in range(N)]

    for n in range(N):
        for m in range(N):
            dfs(map1, n, m, 1, map1[n][m])

    answer = [(i, j) for i, j in ans if max(ans[1]) == j]
    print("#{} {} {}".format(T, min(answer)[0], min(answer)[1]))

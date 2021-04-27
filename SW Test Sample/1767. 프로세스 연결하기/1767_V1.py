def x_axis(visit, x, y, idx):
    temp = []

    if idx == 0:
        for i in range(x):
            temp.append(visit[i][y])
    else:
        for i in range(x + 1, N):
            temp.append(visit[i][y])

    return temp


def dfs(idx, count, core_count):
    global core, N, cnt, core_cnt

    if idx == len(core):
        if core_cnt < core_count:
            core_cnt = core_count

            cnt = float('inf')
            if cnt >= count:
                cnt = count

        if core_cnt == core_count:
            if cnt >= count:
                cnt = count

        return

    x, y = core[idx]

    for i in range(4):
        visit = visit_before

        if i == 0 and 1 not in visit[x][:y]:
            core_count += 1
            for j in range(y):
                count += 1
                visit[x][j] = 1

            dfs(idx + 1, count, core_count)

            core_count -= 1
            for j in range(y):
                count -= 1
                visit[x][j] = 0

        elif i == 1 and 1 not in x_axis(visit, x, y, 0):
            core_count += 1
            for j in range(x):
                count += 1
                visit[j][y] = 1

            dfs(idx + 1, count, core_count)

            core_count -= 1
            for j in range(x):
                count -= 1
                visit[j][y] = 0

        elif i == 2 and 1 not in visit[x][y + 1:]:
            core_count += 1
            for j in range(y + 1, N):
                count += 1
                visit[x][j] = 1

            dfs(idx + 1, count, core_count)

            core_count -= 1
            for j in range(y + 1, N):
                count -= 1
                visit[x][j] = 0

        elif i == 3 and 1 not in x_axis(visit, x, y, 1):
            core_count += 1
            for j in range(x + 1, N):
                count += 1
                visit[j][y] = 1

            dfs(idx + 1, count, core_count)

            core_count -= 1
            for j in range(x + 1, N):
                count -= 1
                visit[j][y] = 0

        else:
            dfs(idx + 1, count, core_count)


for T in range(1, int(input()) + 1):
    N = int(input())
    map1 = [[int(i) for i in input().strip().split()] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visit_before = visited

    core = []
    cnt, core_cnt = float('inf'), 0

    for i in range(N):
        for j in range(N):
            if map1[i][j] == 1:
                visited[i][j] = 1
                core.append((i, j))

    for i, j in core:
        if i == 0 or j == 0:
            core_cnt += 1
            core.remove((i, j))

    dfs(0, 0, core_cnt)
    print("#{} {}".format(T, cnt))

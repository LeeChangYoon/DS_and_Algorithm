def dfs(map1, x, y):
    global ans
    visit[x][y] = 1

    if x == 0:
        ans = y
        return

    for i in range(3):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < size and 0 <= ty < size and map1[tx][ty] == 1 and visit[tx][ty] == 0:
            return dfs(map1, tx, ty)


size = 100  # 나중에 100으로 바꿔줘야 함.
dx = [0, 0, -1]
dy = [-1, 1, 0]

for T in range(10):  # 나중에 10으로 바꿔줘야 함.
    N = int(input())

    map1 = [[int(i) for i in input().strip().split()] for _ in range(size)]
    visit = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        if map1[size - 1][i] == 2:
            end = (size - 1, i)

    ans = -1
    dfs(map1, end[0], end[1])

    print("#{} {}".format(N, ans))

for T in range(1, int(input()) + 1):
    N = int(input())
    map1 = [[int(i) for i in input()] for _ in range(N)]
    ans = 0

    mid = N // 2
    up = N // 2 + 1

    for i in range(up):
        for j in range(mid - i, N - mid + i):
            ans += map1[i][j]

    for i in range(up, N):
        for j in range(i - mid, N - i + mid):
            ans += map1[i][j]

    print("#{} {}".format(T, ans))

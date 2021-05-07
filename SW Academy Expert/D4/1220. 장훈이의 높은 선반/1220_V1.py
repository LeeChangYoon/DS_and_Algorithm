def dp(H):
    global temp, visit, ans
    j, tmp = 0, []

    if len(H) == 0:
        return

    if len(visit) == 0:
        for i in H:
            j += i
            visit.append(j)

    else:
        for i in visit:
            tmp.append(i - temp)
        visit = tmp

    for i in visit:
        if 0 <= i - B <= ans:
            ans = i - B

    temp = H[0]
    del H[0]
    del visit[0]
    dp(H)


visit = []
temp = 0

for T in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = [int(i) for i in input().strip().split()]

    ans = 200000
    visit, temp= [], 0

    dp(H)

    print("#{} {}".format(T, ans))
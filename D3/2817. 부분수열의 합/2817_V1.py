def rec(ans):
    global temp
    temp = 0

    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):
                temp += test[j]

        if temp == K:
            ans += 1
            temp = 0

    return ans


T = int(input())
temp = 0

while T > 0:
    N, K = map(int, input().split())
    test = [int(i) for i in input().strip().split() if int(i) < K]

    temp += 1
    print("#{} {}".format(temp, rec(0)))
    T -= 1

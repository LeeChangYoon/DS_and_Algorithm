for T in range(1, int(input()) + 1):
    cnt = [0] * 201

    for _ in range(int(input())):
        x, y = map(int, input().split())

        if x > y: x, y = y, x
        x = (x + 1) // 2
        y = (y + 1) // 2

        for i in range(x, y + 1):
            cnt[i] += 1

    print("#{} {}".format(T, max(cnt)))

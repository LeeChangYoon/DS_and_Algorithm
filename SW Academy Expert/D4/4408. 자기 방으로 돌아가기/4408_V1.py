for T in range(1, int(input()) + 1):
    N = int(input())
    student = [list(map(int, input().strip().split())) for _ in range(N)]
    cnt = 1

    for i in range(N - 1):
        x, tx = student[i][0], student[i + 1][0]
        y, ty = student[i][1], student[i + 1][1]

        if x % 2 == 0:
            x -= 1
        if y % 2 == 1:
            y += 1

        if x < y:
            if x <= tx <= y or x <= ty <= y:
                cnt += 1
            else:
                pass
        elif x > y:
            if x >= tx >= y or x >= ty >= y:
                cnt += 1
            else:
                pass

    print("#{} {}".format(T, cnt))

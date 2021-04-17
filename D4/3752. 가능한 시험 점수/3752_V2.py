for t in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    check = [1] + [0] * sum(scores)
    visit = [0]

    for i in scores:
        temp = visit[:]
        for j in temp:
            if not check[i + j]:
                check[i + j] = 1
                visit.append(i + j)

    print('#{} {}'.format(t, len(visit)))

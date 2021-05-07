def front_end(n):
    for i in range(1, 142):
        global tmp

        if n == 1:
            return 0
        elif i + (i - 1) * (i - 2) / 2 == n:  # front
            tmp = i
            return 1
        elif i + i * (i - 1) / 2 == n:  # end
            tmp = i - 1
            return -1
        elif i + (i - 1) * (i - 2) / 2 < n < i + i * (i - 1) / 2:
            tmp = i
            return 2


def bfs(idx, queue, cnt):
    global tmp, ans

    if idx > 10000:
        return
    elif b == idx:
        ans = 0
        return 0

    k = front_end(idx)

    if k == 0:
        queue = [2, 3]

        if b in queue:
            ans = cnt + 1
            return cnt + 1
        else:
            for i in queue:
                if visit[i] == 0:
                    visit[i] = 1
                    bfs(i, [], cnt + 1)

    elif k == 1:
        num1 = idx - tmp - 1
        num2 = idx + tmp

        if idx > b:
            queue = [num1]
        elif idx < b:
            queue = [idx + 1, num2, num2 + 1]

        if b in queue:
            ans = cnt + 1
            return cnt + 1
        else:
            for i in queue:
                if visit[i] == 0:
                    visit[i] = 1
                    bfs(i, [], cnt + 1)

    elif k == -1:
        num1 = idx - tmp
        num2 = idx + tmp + 1

        if idx > b:
            queue = [num1, idx + 1]
        elif idx < b:
            queue = [num2, num2 + 1]

        if b in queue:
            ans = cnt + 1
            return cnt + 1
        else:
            for i in queue:
                if visit[i] == 0:
                    visit[i] = 1
                    bfs(i, [], cnt + 1)

    elif k == 2:
        num1 = idx - tmp
        num2 = idx + tmp

        if idx > b:
            queue = [num1, num1 + 1, idx - 1]
        elif idx < b:
            queue = [idx + 1, num2, num2 + 1]

        if b in queue:
            ans = cnt + 1
            return cnt + 1
        else:
            for i in queue:
                if visit[i] == 0:
                    visit[i] = 1
                    bfs(i, [], cnt + 1)


cnt = 0
tmp = 0
ans = 0
visit = [0 for i in range(10000)]

for T in range(1, int(input()) + 1):  # T is the number of the test case
    a, b = map(int, input().split())  # a is the current room, b is the target

    res = bfs(a, [], 0)

    print("#{} {}".format(T, ans))

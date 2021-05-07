temp = []


def rotate(n, x, y, r, cnt, idx):
    global temp

    count = 0

    if cnt == 0:
        return

    # Left
    for i in range(x, n):
        idx += 1
        temp[i][y] = idx

    # Bottom
    for i in temp[n - 1]:
        if i == 0:
            count += 1

    for i in range(y + 1, y + 1 + count):
        idx += 1
        temp[n - 1][i] = idx

    # Right
    for i in range(n - 2, x, -1):
        idx += 1
        temp[i][r] = idx

    rotate(n - 1, x + 2, y + 1, r - 1, cnt - 1, idx)


def solution(n):
    global temp
    answer = []
    temp = []

    for i in range(1, n + 1):
        temp.append([0] * i)

    cnt = (n - 1) // 3 + 1
    rotate(n, 0, 0, -1, cnt, 0)

    for i in temp:
        answer += i

    return answer
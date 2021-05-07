def move(arr):
    length = len(arr)

    for i in range(length):
        if arr[i] == 0:
            del arr[i]
            arr.append(0)

    for i in range(length - 1):
        if arr[i] == arr[i + 1]:
            arr[i] *= 2
            arr[i + 1] = 0

    for i in range(length):
        if arr[i] == 0:
            del arr[i]
            arr.append(0)

    return arr


def find():
    temp = S[text]
    map1_tmp = [[] for _ in range(N)]
    tmp = []

    if temp == 0:
        for i in range(N):
            map1_tmp.append(move(map1[i]))
        return map1_tmp

    elif temp == 1:
        for i in range(N):
            map1[i].reverse()
            map1_tmp.append(move(map1[i]))
        return map1_tmp

    elif temp == 2:
        for i in range(N):
            for j in range(N):
                tmp.append(map1[j][i])

            tmp = move(tmp)
            for j in range(N):
                map1_tmp[j].append(tmp[j])
            tmp = []

        return map1_tmp

    elif temp == 3:
        for i in range(N):
            for j in range(N):
                tmp.append(map1[j][i])
                tmp.reverse()

            tmp = move(tmp)
            tmp.reverse()
            for j in range(N):
                map1_tmp[j].append(tmp[j])
            tmp = []

        return map1_tmp


S = {"left": 0, "right": 1, "up": 2, "down": 3}
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for T in range(1, int(input()) + 1):
    N_tmp, text = input().strip().split()
    N = int(N_tmp)
    map1 = [[int(i) for i in input().strip().split()] for _ in range(N)]

    res = find()

    print("#{}".format(T))

    for i in range(N):
        for j in range(N):
            print(res[i][j], end=' ')
        print()
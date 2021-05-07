def next(arr, visit, dir, num, pos):
    while pos:
        item = arr[pos[0]][pos[1]]

        # 프로그램 정지
        if item == '@':
            return True

        # 동일한 방문 정보 --> 무한반복이므로 반복문 종료
        if (dir, num) in visit[pos[0]][pos[1]]:
            return False
        visit[pos[0]][pos[1]].append((dir, num))

        if item == '?':
            temp = ['>', '<', '^', 'v']

            while temp:
                nextDir = temp.pop()
                if next(arr, visit, nextDir, num, nextPos(nextDir, pos)):
                    return True

        else:
            # 숫자 처리
            if item.isdigit():
                num = int(item)

            elif item in ['>', '<', '^', 'v']:
                dir = item

            elif item == '_':
                if num == 0: dir = '>'
                else: dir = '<'

            elif item == '|':
                if num == 0: dir = 'v'
                else: dir = '^'

            elif item == '+':
                if num == 15: num = 0
                else: num += 1

            elif item == '-':
                if num == 0: num = 15
                else: num -= 1

            pos = nextPos(dir, pos)


def nextPos(dir, current):
    direction = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    r, c = current

    temp_r, temp_c = direction[dir]
    temp_r += r
    temp_c += c

    if temp_r < 0 or temp_r >= R or temp_c < 0 or temp_c >= C:
        if dir == '<': temp_c = C - 1
        elif dir == '>': temp_c = 0
        elif dir == 'v': temp_r = 0
        elif dir == '^': temp_r = R - 1

    return (temp_r, temp_c)


def solve(arr, visit):
    end = 0
    end_point = []

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '@':
                end += 1
                end_point.append((i, j))

    if end < 1:
        return 'NO'

    for pos in end_point:
        r, c = pos
        top_bottom = [(-1, 0), (1, 0)]
        left_right = [(0, 1), (0, -1)]
        bad_count = 0

        for add in top_bottom:
            tr = r + add[0]
            tc = c + add[1]

            if 0 <= tr < R and 0 <= tc < C:
                if arr[tr][tc] in ['>', '<']:
                    bad_count += 1
                else:
                    bad_count = 0
                    break

        for add in left_right:
            tr = r + add[0]
            tc = c + add[1]

            if 0 <= tr < R and 0 <= tc < C:
                if arr[tr][tc] in ['^', 'v']:
                    bad_count += 1
                else:
                    bad_count = 0
                    break

            if bad_count == 4:
                end -= 1

        if end < 1:
            return 'NO'
        if next(arr, visit, '>', 0, (0, 0)):
            return 'YES'
        else:
            return 'NO'


for T in range(1, int(input()) + 1):
    arr = []
    R, C = map(int, input().split())

    for _ in range(R):
        arr.append(list(input().strip()))

    visit = [[[] for _ in range(C)] for i in range(R)]
    print("#{} {}".format(T, solve(arr, visit)))

def findcores(board):
    fix = 0
    cores = []
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                    fix += 1
                else:
                    cores.append((r, c))
    return fix, cores


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def cancel(row, col, idx, plus):
    dr, dc = delta[idx]
    for _ in range(plus):
        board[row + dr][col + dc] = 0
        row += dr
        col += dc


def install(row, col, idx):
    _row = row
    _col = col
    dr, dc = delta[idx]
    plus = 0
    while 0 <= row + dr < N and 0 <= col + dc < N:
        row += dr
        col += dc
        if board[row][col]:
            break
        board[row][col] = 1
        plus += 1
    else:
        return plus
    cancel(_row, _col, idx, plus)
    return 0


def DFS(now, last, code):
    global maxCores, minCode
    if maxCores < len(now):
        maxCores = len(now)
        minCode = 12 * 12 + 1
    if maxCores == len(now) and minCode > code:
        minCode = code

    for i in range(last, len(cores)):
        for idx in range(4):
            plus = install(*cores[i], idx)
            if not plus:
                continue
            next = now[:]
            next.append(i)
            DFS(next, i + 1, code + plus)
            cancel(*cores[i], idx, plus)


for T in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    fix, cores = findcores(board)
    maxCores = -1
    minCode = 12 * 12 + 1
    DFS([], 0, 0)
    print('#{} {}'.format(T, minCode))
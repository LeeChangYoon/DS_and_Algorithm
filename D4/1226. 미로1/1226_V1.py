'''
온전히 내 힘으로 푼 첫번째 DFS문제.
기본 문제이기도 하고 코드가 더럽지만 처음부터 끝까지 내 힘으로 푼 문제라 감회가 새롭다.
이 문제를 기점으로 DFS & 완전탐색 기법을 어떻게 사용해야 하는지 확실히 알게 된 계기가 된 것 같다.
'''

def dfs(map1, x, y):
    global ans

    # When it arrives at the end point
    if x == end[0] and y == end[1]:
        ans = 1

    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < 16 and 0 <= ty < 16:
                if map1[tx][ty] == 1 or map1[tx][ty] == 2:
                    continue

                elif map1[tx][ty] == 0 or map1[tx][ty] == 3:
                    if visit[tx][ty] == 0:
                        visit[tx][ty] = 1
                        dfs(map1, tx, ty)
                    else:
                        continue

        else:
            return 0


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(10):
    T = int(input())  # Index of the test case.
    map1 = [[int(i) for i in input()] for _ in range(16)]  # map1 size id 16 x 16
    visit = [[0 for _ in range(16)] for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if map1[i][j] == 2:
                start = (i, j)
            elif map1[i][j] == 3:
                end = (i, j)

    ans = 0
    dfs(map1, start[0], start[1])

    if ans == 1:
        print("#{} {}".format(T, ans))
    else:
        print("#{} {}".format(T, 0))

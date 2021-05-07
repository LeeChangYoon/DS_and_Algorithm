'''
이것도 DFS 를 이용한 탐색 문제였다.
왜 계속 DFS 문제만 나오면 위축되고, 이를 어떻게 이용해야 하는지 대해 모르는 것 같지?

이걸로 좀 명확해진 것 같다. DFS & BFS 를 정확히 다시 공부하자!
맵에서 DFS 를 이용해 탐색하는 방법을 배우게 된 문제였던 것 같다.
'''

def dfs(idx, row, col, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    num += test[row][col]

    if idx == 6:
        result.append(num)
        return

    for i in range(4):
        if 0 <= row + dx[i] < 4 and 0 <= col + dy[i] < 4:
            dfs(idx + 1, row + dx[i], col + dy[i], num)


for T in range(1, int(input()) + 1):
    test = [list(map(str, input().split())) for _ in range(4)]
    result = []

    for x in range(4):
        for y in range(4):
            dfs(0, x, y, "")

    answer = set(result)
    print('#{} {}'.format(T, len(answer)))
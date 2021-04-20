'''
처음에는 DFS 로 접근 해야 하는 문제인 줄 알았다.
다익스트라 알고리즘도 생각이 났는데 구체적인 구현 방법이 기억이 안나서 사용하지 않았다.

DFS의 경우 이제 상하좌우 방향으로 탐색을 하는데, 그러면 데이터 값도 너무 커지고 어떤 방향으로 구현을 해야 할지 딱 떠오르는게 없었다.
그래서 BFS로 접근했다.

오늘 배운 점:
1. from _collection import deque
2. dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
3. queue에 값을 대입하여 popleft() 했을때 이미 저장해 놓은 key값과 비교했을때 더 작다면 (즉, 어떤 경로로든 그 점에 왔을때 이미 저장된 값보다 작다면),
   그 값을 key값으로 정하고 다음 탐색을 이어나간다.
'''

from _collections import deque

for tc in range(1, 1 + int(input())):
    n = int(input())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    answer = 0
    
    keys = [[99999] * n for _ in range(n)]
    keys[0][0] = 0  # 시작점은 0
    q = deque()
    q.append((0, 0))

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if keys[x][y] + maps[nx][ny] < keys[nx][ny]:
                    keys[nx][ny] = keys[x][y] + maps[nx][ny]
                    q.append((nx, ny))

    answer = keys[-1][-1]

    print('#{} {}'.format(tc, answer))

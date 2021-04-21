'''
이 문제는 처음에 DFS로 접근했다.
그러다 곰곰히 생각 해보다 DFS로 접근 할 경우 이미 사용한 값을 다시 사용해 뭔가 효율적이지 않다는 생가기 들긴 했지만
일단 구현해 봤다.

사실 이때 BFS로 풀이를 바꿔 DP & BFS를 이용해 문제를  풀어야 했다.

여튼 input값에 대한 output은 제대로 나왔지만 역시 RunTime Error가 떴다 ㅠㅠ.
'''


def dfs(map1, x, y, cnt, target):
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < N and 0 <= ty < N and map1[x][y] + 1 == map1[tx][ty]:
            cnt += 1
            return dfs(map1, tx, ty, cnt, target)

    else:
        ans.append((target, cnt))


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


for T in range(1, int(input()) + 1):
    ans = []
    N = int(input())
    map1 = [[int(i) for i in input().strip().split()] for _ in range(N)]

    for n in range(N):
        for m in range(N):
            dfs(map1, n, m, 1, map1[n][m])

    answer = [(i, j) for i, j in ans if max(ans[1]) == j]
    print("#{} {} {}".format(T, min(answer)[0], min(answer)[1]))

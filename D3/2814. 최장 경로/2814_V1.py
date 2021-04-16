'''
DFS 를 이용하는 문제였다.
계속 DFS 인걸 모르고 접근 하려다가 낭페를 본 다음 DFS 로 풀려고 하는 것 같다.
사실 이번 문제는 그래프도 몰랐고, 그 그래프를 이용해 DFS 를 이용해야 한다는 사실도 몰랐다.
좀 더 솔직하게 말하자면 그냥 문제 자체를 이해하지 못한 것 같다.

이 문제를 통해 그래프에 대해 공부하고, DFS 에 대한 개념에 대해 더 정확하게 알게 된 계기가 된 것 같다.
따라서 이 문제를 푼 후, DFS 그리고 그래프에 대해 다시 한번 공부해야 겠다고 느꼇다.
'''

def dfs(idx, ans):
    global answer

    visited[idx] = 0
    ans += 1

    if answer < ans: answer = ans

    for i in graph[idx]:
        if visited[i]: dfs(i, ans)

    visited[idx] = 1


T = int(input())
tmp = 0

while T > 0:
    N, M = map(int, input().split())
    visited = [1 for _ in range(N + 1)]

    temp = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N + 1)]
    answer = 0

    for a, b in temp:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):  dfs(i, 0)

    tmp += 1
    print('#{} {}'.format(tmp, answer))
    T -= 1

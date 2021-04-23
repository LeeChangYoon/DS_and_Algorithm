'''
그냥 그런저런 DFS 탐색 문제였다.
그런데 이제 그냥 완전탐색으로 문제를 풀긴 했지만, 하나 또 하고 싶은건 이제 BackTracing이다.
항상 DFS 알고리즘을 작성하면서 느끼는 건데, 함수 내에서 어떤 기준을 충족했을 때 (예를 들면, 원하는 값에 도달 했다던가, 아니면 도착점에 도착 했다던가...)
함수를 종료시키는 법을 아직까지 정확히 알지 못한 것 같다.
이걸 어디서 알 수 있을까...?
'''

def dfs(n):
    global ans

    if n == 99:
        ans = 1

    else:
        if n in node:
            for i in node[n]:
                dfs(i)


for _ in range(10):  # 나중에 10으로 고쳐줘야 함
    T, N = map(int, input().split())
    vertex = [int(i) for i in input().strip().split()]
    node = {}
    ans = 0

    for i in range(N):
        if vertex[2 * i] not in node:
            node[vertex[2 * i]] = [vertex[2 * i + 1]]
        else:
            node[vertex[2 * i]].append(vertex[2 * i + 1])

    dfs(0)
    print("#{} {}".format(T, ans))

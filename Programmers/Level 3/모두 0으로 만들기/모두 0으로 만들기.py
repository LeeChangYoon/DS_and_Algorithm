import sys

sys.setrecursionlimit(10 ** 7)


def solution(a, edges):
    if sum(a):
        return -1

    cp_link = [list() for i in range(len(a))]

    visited = [0] * len(a)
    for i in range(len(edges)):
        cp_link[edges[i][0]].append(edges[i][1])
        cp_link[edges[i][1]].append(edges[i][0])
    global answer
    answer = 0

    def preorder(node):
        global answer
        if visited[node]:
            return 0

        visited[node] = 1
        for i in range(len(cp_link[node])):
            a[node] += preorder(cp_link[node][i])

        son = a[node]
        a[node] = 0
        answer += abs(son)
        return son

    preorder(0)
    if not a[0]:
        return answer
    return -1
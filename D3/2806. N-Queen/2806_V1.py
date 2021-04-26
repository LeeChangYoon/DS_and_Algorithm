'''
되게 유명한 문제인 N-Queen 문제이다.
DFS로 풀면 되며 다음 queen을 검사할 때 이전 Queen과 가로, 왼쪽 오른쪽 대각선에 Queen이 안 만나는 지만 검사 해줘서 풀면 되는 문제이다. 
'''


def dfs(x):
    global answer

    if x == n:
        answer += 1
        return

    for y in range(n):
        if y in columns or x + y in l_diagonals or x - y in r_diagonals:
            continue
        columns.add(y)
        l_diagonals.add(x + y)
        r_diagonals.add(x - y)
        dfs(x + 1)
        columns.remove(y)
        l_diagonals.remove(x + y)
        r_diagonals.remove(x - y)


for T in range(1, int(input()) + 1):
    answer = 0
    n = int(input())
    columns, l_diagonals, r_diagonals = set(), set(), set()
    dfs(0)
    print("#{} {}".format(T, answer))

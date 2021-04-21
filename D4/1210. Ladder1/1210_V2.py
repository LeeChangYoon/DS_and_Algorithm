'''
이번 문제는 DFS를 사용하는게 딱 눈에 보였다.
V1, V2 둘 다 큰 차이점은 없는데 그냥 dfs 함수에 불필요한 값들이 들어 있냐 없냐 차이이다.
그것 때문에 RunTime Error가 떴다 ㅠㅠ.

이번 문제에서 배운 점
1. dfs 백트랙킹 & 완전탐색 --> 완전탐색을 하고 싶은 경우 V1 처럼 코드 뒤에 구문을 붙여주면 된다.
2. if문 조건을 붙여 dfs 탐색을 끝내는 방법.
'''

'''
Test Case (size: 10)
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1 
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1 
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1 
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2
'''

def dfs(map1, x, y):
    global ans
    visit[x][y] = 1

    if x == 0:
        ans = y
        return

    for i in range(3):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < size and 0 <= ty < size and map1[tx][ty] == 1 and visit[tx][ty] == 0:
            return dfs(map1, tx, ty)


size = 100  # 나중에 100으로 바꿔줘야 함.
dx = [0, 0, -1]
dy = [-1, 1, 0]

for T in range(10):  # 나중에 10으로 바꿔줘야 함.
    N = int(input())

    map1 = [[int(i) for i in input().strip().split()] for _ in range(size)]
    visit = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        if map1[size - 1][i] == 2:
            end = (size - 1, i)

    ans = -1
    dfs(map1, end[0], end[1])

    print("#{} {}".format(N, ans))

'''
처음에는 부분 집합들을 모두 구해 하나씩 더해 목표 값과 비교 후 그 갯수를 일일이 새어 보려고 했다.
물론 원하던 output 값은 나왔지만, RunTime Error가 났다.

그래서 다른 방법을 생각하던 중 DFS를 생각했지만, 어떻게 해야 할 지 몰랐다.
'''

def rec(ans):
    global temp
    temp = 0

    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):
                temp += test[j]

        if temp == K:
            ans += 1
            temp = 0

    return ans


T = int(input())
temp = 0

while T > 0:
    N, K = map(int, input().split())
    test = [int(i) for i in input().strip().split() if int(i) < K]

    temp += 1
    print("#{} {}".format(temp, rec(0)))
    T -= 1

'''
이 코드가 구글링을 통해 가져온 코드이다.
내가 어디서 가지치기를 생각 못했는지 알았다.
매번 공부할 때마다 내가 많이 부족하다고 느낀다.
더 열심히 해야지!
'''

def find(left, right, depth, state):
    if depth == N:
        return 1

    if (D[state] > 0):
        return D[state]

    cnt = 0
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            cnt += find(left + test[i], right, depth + 1, state + mul[i])

            if left >= right + test[i]:
                cnt += find(left, right + test[i], depth + 1, state + mul[i] * 2)

            visit[i] = False

    D[state] = cnt
    return cnt


for T in range(1, int(input()) + 1):
    N = int(input())
    test = list(map(int, input().split()))
    visit = [0] * 10
    ans = 0

    mul = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]
    D = [0] * (mul[N])

    print("#{} {}".format(T, find(0, 0, 0, 0)))

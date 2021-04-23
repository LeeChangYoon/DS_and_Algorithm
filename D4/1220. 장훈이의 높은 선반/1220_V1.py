'''
처음에 문제를 보자마자 동작할당을 이용해야 한다고 생각이 빡 들었고
그 다음에 중복되는 수가 하나씩 줄고 그 이전에 기준값을 사용하여 전에 사용했던 데이터들에서 그 값을 빼주면 답이 나온다고 생각하였다.
근데 왜 TestCase 10개 중에 3개만 맞았는지 모르겠다...
'''

def dp(H):
    global temp, visit, ans
    j, tmp = 0, []

    if len(H) == 0:
        return

    if len(visit) == 0:
        for i in H:
            j += i
            visit.append(j)

    else:
        for i in visit:
            tmp.append(i - temp)
        visit = tmp

    for i in visit:
        if 0 <= i - B <= ans:
            ans = i - B

    temp = H[0]
    del H[0]
    del visit[0]
    dp(H)


visit = []
temp = 0

for T in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = [int(i) for i in input().strip().split()]

    ans = 200000
    visit, temp= [], 0

    dp(H)

    print("#{} {}".format(T, ans))

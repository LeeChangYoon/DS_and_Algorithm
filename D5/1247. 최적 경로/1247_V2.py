'''
다른 사람의 풀이를 참고한 V2이다.
아까 언급했지만, TSP & DP를 이용한 코드이다.
사실 지금 이 순간에도 이 코드가 완전히 이해되지는 않는다.
대충 아 TSP & DP를 이용하면 저런식으로 코드가 진행되는 지만 알 것 같다.
차후에 TSP를 더 깊게 공부해 봐야 정확하게 알 수 있다고 말할 수 있을 것 같다.

이번 문제를 통해 배운점:
1. TSP & DP를 사용해 문제를 푸는 것
2. float('inf') --> infinite
3. TSP & DP를 풀 때에는 Bitmasking을 통해 풀어야 한다는 것 (이 부분이 아직까지 정확하게 이해 가지가 않는다.)

더 공부해야 할 점:
1. Bitlen은 왜 있고 왜 사용되는가?
2. TSP & Greedy, TSP Linear, TSP & DP
'''

for test in range(1, int(input()) + 1):
    N = int(input())
    info = list(map(int, input().split()))

    start = (info[0], info[1])
    end = (info[2], info[3])

    distance = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            distance[i][j] = distance[j][i] = abs(info[2 * i + 4] - info[2 * j + 4]) + abs(info[2 * i + 5] - info[2 * j + 5])

    bitmask = [[0] * N for _ in range(1 << N)]
    bitlen = [0]

    for _ in range(N):
        bitlen += [num + 1 for num in bitlen]

    for num in range(N):
        bitmask[1 << num][num] = abs(start[0] - info[2 * num + 4]) + abs(start[1] - info[2 * num + 5])

    for length in range(2, N + 1):
        for idx in range(1, 1 << N):
            if bitlen[idx] != length:
                continue

            members = [i for i in range(N) if idx & (1 << i)]

            for member in members:
                shortcut = float('inf')
                for rest in members:
                    if rest == member:
                        continue

                    shortcut = min(shortcut, bitmask[idx - (1 << member)][rest] + distance[rest][member])

                bitmask[idx][member] = shortcut

    ans = float('inf')
    for n in range(N):
        ans = min(ans, bitmask[-1][n] + abs(end[0] - info[2 * n + 4]) + abs(end[1] - info[2 * n + 5]))
    print('#{} {}'.format(test, ans))

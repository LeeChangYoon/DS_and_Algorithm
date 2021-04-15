def dfs(idx, sum):
    global cnt

    if idx == N:
        return
    if sum + test[idx] == K:
        cnt += 1

    dfs(idx + 1, sum)
    dfs(idx + 1, sum + test[idx])


T = int(input())
temp = 0

while T > 0:
    N, K = map(int, input().split())
    test = [int(i) for i in input().strip().split()]

    cnt = 0
    dfs(0, 0)
    temp += 1
    print("#{} {}".format(temp, cnt))
    T -= 1

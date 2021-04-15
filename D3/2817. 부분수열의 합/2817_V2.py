'''
그래서 열심히 다른 방법을 찾은 결과 DFS와 BackTracking을 사용하기 로 했다.
이 기법은 DFS로 모든 트리를 방문하여 원하는 답이 있으면 count하는 방식의 코드이다.
'''

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

'''
왜 10개의 TestCase 중에서 3개만 맞았는지 확인해 봤더니 어떠한 기준값을 잡았을 때
이 값을 더할수도, 안더할 수도 있다는 것을 간과했음을 알았다.
그래서 2개의 함수를 실행하는데 하나는 다음값을 더하는 것, 다른 하나는 더하지 않는 것 이렇게 2개를 재귀함수를 작성하였다. 
'''

T = int(input())

def dp(idx, height):
    global min_height
    # B와 크거나 같고 최소값보다 작은 경우에만 갱신
    if B <= height < min_height:
        min_height = height
    if idx == N:
        return
    # 해당 인덱스의 키를 포함시키지 않는 경우
    dp(idx+1, height)
    # 해당 인덱스의 키를 포함시키는 경우
    dp(idx+1, height + height_lst[idx])

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height_lst = list(map(int, input().split()))
    # N의 최대값 20, B의 최대값이 10000이므로 200000으로 초기화
    min_height = 200000
    dp(0, 0)
    print('#{} {}'.format(tc, min_height - B))

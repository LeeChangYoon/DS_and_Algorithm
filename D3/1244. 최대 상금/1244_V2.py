'''
완전 탐색을 사용하여 틀린 저번 코드를 보안한 DFS를 이용한 코드이다.

DFS로 먼저 깊이 들어가 가장 큰 숫자를 찾아준 뒤, 그 과정들 중 나온 숫자들을 기록해 두었다가 
다음 Tree 방문시 중복된 숫자들이 있으면 바로 넘겨 처리 속도를 높여준 코드이다.

새로 안 사실:
1. Visited Dictionary를 이용한 DFS 알고리즘 구현
2. ''.join(values) 으로 바로 string을 int형으로 변환해 준 것.
3. visited.get((temp_key, count - 1), 1)
4. print('#{} {}'.format(t + 1, answer))
'''

def dfs(count):
    global answer

    if not count:
        temp = int(''.join(values))

        if answer < temp:
            answer = temp
        return

    for i in range(length):
        for j in range(i + 1, length):
            values[i], values[j] = values[j], values[i]
            temp_key = ''.join(values)

            if visited.get((temp_key, count - 1), 1):
                visited[(temp_key, count - 1)] = 0
                dfs(count - 1)

            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}

    dfs(change)
    print('#{} {}'.format(t + 1, answer))

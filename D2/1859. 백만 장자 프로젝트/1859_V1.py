'''
처음 풀었을 때 분할 정복을 통해 문제를 풀어야 겠다고 생각 했다.
그래서 앞에서 부터 처리 하기 위해 맨 앞을 기준으로 분할을 하기 시작했는데
RunTime Error가 났다.

어디가 문제인지 보기 위해 봤더니 데이터 크기가 커지면 처리 시간이 오래 걸린다는 걸 발견했다.
'''

def f(data, res):
    global MAX, idx, amount, price
    MAX, idx, amount, price = 0, 0, 0, 0

    MAX = max(data)
    idx = data.index(MAX)

    for i in data[:idx]:
        price += i
        amount += 1
    res += amount * MAX - price

    if idx == len(data) - 1:
        return res

    else:
        data = data[idx + 1:]
        return f(data, res)


cnt = int(input())
temp = 0

while cnt > 0:
    num = int(input())
    data = [int(i) for i in input().strip().split()]

    temp += 1
    ans = f(data, 0)
    print("#" + str(temp) + " " + str(ans))

    cnt -= 1

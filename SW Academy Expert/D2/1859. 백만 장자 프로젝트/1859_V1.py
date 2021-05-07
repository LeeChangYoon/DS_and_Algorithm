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

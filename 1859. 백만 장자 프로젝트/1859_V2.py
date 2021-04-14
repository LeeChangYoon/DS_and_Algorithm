def f(data, res, MAX):
    data.reverse()

    for i in range(1, len(data)):
        if MAX < data[i]:
            MAX = data[i]
            data = data[i:]
            data.reverse()
            return f(data, res, MAX)
        else:
            res += MAX - data[i]

    return res


cnt = int(input())
temp = 0

while cnt > 0:
    num = int(input())
    data = [int(i) for i in input().strip().split()]

    temp += 1
    ans = f(data, 0, data[-1])
    print("#" + str(temp) + " " + str(ans))

    cnt -= 1

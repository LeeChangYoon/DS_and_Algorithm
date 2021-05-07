def f(data, loop, idx, res):
    if loop == 0:
        return res + data

    else:
        if (len(data)) < 2:
            res = res + data
            temp = res[-1]
            res[-1] = res[-2]
            res[-2] = temp
            return f([], loop - 1, 0, res)

        MAX = max(data)

        if data[idx] == MAX:
            res.append(data[idx])
            return f(data[idx + 1:], loop, 0, res)

        else:
            tmp_max = [i for i in range(len(data)) if data[i] == MAX]
            tmp_min = [i for i in range(tmp_max[-1] + 1) if data[0] > data[i]]

            temp = data[idx]
            data[idx] = data[tmp_max[-1-len(tmp_min)]]
            data[tmp_max[-1 - len(tmp_min)]] = temp

            return f(data, loop - 1, 0, res)



cnt = int(input())
temp, idx = 0, 0

while cnt > 0:
    num, loop = map(int, input().split())
    data = [int(i) for i in str(num)]
    res = []

    ans = f(data, loop, 0, res)

    temp += 1
    answer = ""
    for i in ans:
        answer += str(i)
    print("#" + str(temp) + " " + answer)
    cnt -= 1

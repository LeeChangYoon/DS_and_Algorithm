'''
이 문제 같은 경우에는 처음에 생각 나는게 완전 탐색을 통한 답 구하기였다.
그래서 생각나는게 저거 뿐이라 조건 하나하나 다 따져서 if문과 for문을 남발하여
결국에 RunTime Error가 난 것 같다. (실제로 Test Case 10개 중 5개만 맞음)
'''

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

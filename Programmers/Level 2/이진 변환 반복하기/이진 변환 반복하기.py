def conv(s, cnt, cnt_zero):
    if s == "1":
        return cnt, cnt_zero

    tmp = ""

    for i in s:
        if i == "0":
            cnt_zero += 1
        else:
            tmp += i

    cnt += 1
    return conv(str(bin(len(tmp))[2:]), cnt, cnt_zero)


def solution(s):
    answer = list(conv(s, 0, 0))
    return answer
# 중복된 원가 있을 수 있다
# 원소에 정해진 순서가 있다
# 원소의 개수는 유한이다


def solution(s):
    answer = []
    s_tmp = ""
    tmp = []
    temp = []
    s = s[1:-1]

    for i in s:
        if i == "{":
            s = ""
            continue

        if (i == "," or i == "}") and len(s_tmp) != 0:
            temp.append(int(s_tmp))
            s_tmp = ""

        if i == "}":
            tmp.append(temp)
            temp = []

        if i in [",", "{", "}"]:
            pass
        else:
            s_tmp += i

    tmp.sort(key=len)

    for i in tmp:
        for j in i:
            if j in answer:
                continue
            else:
                answer.append(j)

    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
'''
V1의 단점을 보안하기 위해 작성한 코드이다.
처리 시간이 길어지는 걸 막기 위해 앞에서 부터 분할 정복 하던걸 뒤에서 부터 해보았다.
그러니 데이터 크기가 커져도 괜찮다는 것을 알았다.

1. 배열중 가장 큰 값을 찾고 그 값보다 앞에 있는 값들과 차이만큼 결과값에 ++ 합니다.
2. 그 후, 가장 큰 값과 앞에 있는 값들을 모두 배열에서 제외한 새로운 배열을 만듭니다. 배열의 크기가 0이나 1이 될 때까지 1, 2 반복

이렇게 하면 반복문 개수가 줄어든다.
'''
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

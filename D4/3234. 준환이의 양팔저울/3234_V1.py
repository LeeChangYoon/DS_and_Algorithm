'''
TestCase 20개중 18개만 맞고 나머지 2개에 대해선 RunTimeError가 발생해 처음에 틀린 문제
왜 틀렸는지 모르겠어서 구글에 찾아보니 내가 가지치기를 제대로 안하고 완전탐색으로 풀어서 그랬다는 것을 확인했다.
물론 for문에 3개라 복잡도가 O(N^3)이라는 것을 알고 있었고 시간 초과로 문제를 틀릴 것을 알고 있었다.
그럼에도 다른 방법을 몰라 일단 이렇게 푼 문제였던 것 같다.
'''

from itertools import permutations


def fac(num):
    if num == 1:
        return num
    return num * fac(num - 1)


def find():
    global cnt
    cnt = 0

    for temp in list(permutations(test, N)):
        for bit_mask in range(1, 2 ** N):
            left, right = 0, 0
            left_cnt, right_cnt = 0, 0

            for i in range(N):
                if (1 << i) & bit_mask:
                    left += temp[i]
                    left_cnt += 1
                else:
                    right += temp[i]
                    right_cnt += 1

                if left >= right:
                    continue
                else:
                    break

            if left >= right:
                cnt += 1


for T in range(1, int(input()) + 1):
    N = int(input())
    test = [int(i) for i in input().strip().split()]
    cnt = 0

    find()

    print("#{} {}".format(T, cnt))

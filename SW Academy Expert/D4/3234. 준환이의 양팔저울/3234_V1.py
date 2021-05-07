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

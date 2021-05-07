# Make the divided array
def make(arr, x1, x2, y1, y2):
    temp = []

    for i in range(x1, x2):
        tmp = []
        for j in range(y1, y2):
            tmp.append(arr[i][j])
        temp.append(tmp)

    return temp


# Divide map into 4 piece and check if each pieces are abstracted or not
def check(arr, res):
    tmp = sum(arr, [])
    if tmp.count(1) == len(tmp):
        res[1] += 1
        return
    elif tmp.count(0) == len(tmp):
        res[0] += 1
        return

    x1, x2 = len(arr) // 2, len(arr)
    y1, y2 = len(arr) // 2, len(arr)

    arr1 = make(arr, 0, x1, 0, y1)
    arr2 = make(arr, 0, x1, y1, y2)
    arr3 = make(arr, x1, x2, 0, y1)
    arr4 = make(arr, x1, x2, y1, y2)

    temp = [arr1, arr2, arr3, arr4]

    for i in temp:
        tmp = sum(i, [])
        if tmp.count(1) == len(tmp):
            res[1] += 1
        elif tmp.count(0) == len(tmp):
            res[0] += 1
        else:
            check(i, res)


# Main solution
def solution(arr):
    answer = [0, 0]
    check(arr, answer)

    return answer
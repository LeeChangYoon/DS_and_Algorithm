import math
p = {True: "Alice", False: "Bob"}

for T in range(1, int(input()) + 1):
    N = int(input())
    x = 1

    win = True
    idx = True

    if N <= 3:
        if N == 1:
            print("#{} {}".format(T, p[False]))
        else:
            print("#{} {}".format(T, p[True]))
        continue

    else:
        depth = math.floor(math.log(N, 2))

        if depth % 2 == 0:
            idd = False
            win = False

    for i in range(depth):
        if idx:
            x += 2
        else:
            x += 2
            x += 1

        idx = not idx

    if x > N:
        win = not win

    print("#{} {}".format(T, p[win]))


# 1 4 4 16 16...

p = {True: "Alice", False: "Bob"}

for T in range(1, int(input()) + 1):
    N = int(input())
    x = 1
    win = True

    while N > 0:
        N -= x

        if win:
            x *= 4
        win = not win

    print("#{} {}".format(T, p[win]))




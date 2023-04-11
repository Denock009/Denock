n = int(input())
k = n
if 1 <= n:
    while True:
        if 3 * k < n:
            print(k, 3 * k)
            break
        else:
            k += 1
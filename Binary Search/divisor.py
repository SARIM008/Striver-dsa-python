import math

def divisor(arr, lim):
    l = 1
    h = max(arr)
    ans = -1

    if len(arr) > lim:
        return -1

    while l <= h:
        m = (l + h) // 2

        t = sum(math.ceil(a / m) for a in arr)

        if t <= lim:
            ans = m
            h = m - 1
        else:
            l = m + 1

    return ans


arr = [1, 2, 3, 4, 5]
lim = 8

print(divisor(arr, lim))
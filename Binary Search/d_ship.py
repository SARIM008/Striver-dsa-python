def ship(arr, d):
    l = max(arr)      # minimum possible capacity
    h = sum(arr)      # maximum possible capacity
    ans = h

    while l <= h:
        m = (l + h) // 2

        days = 1
        load = 0

        for i in arr:
            if load + i > m:
                days += 1
                load = i
            else:
                load += i

        if days <= d:
            ans = m
            h = m - 1
        else:
            l = m + 1

    return ans


arr = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5

print(ship(arr, d))
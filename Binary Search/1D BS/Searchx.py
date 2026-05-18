def search(arr, t):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [3, 4, 6, 7, 9, 12, 16, 17]
t = 6

print(search(arr, t))
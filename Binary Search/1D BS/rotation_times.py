def time_rotated(arr):
    l = 0
    h = len(arr)-1
    mini = float('inf')
    i=0

    while l <= h:

        # entire part sorted
        if arr[l] <= arr[h]:
            mini = min(mini, arr[l])
            break

        m = (l+h)//2

        # left half sorted
        if arr[l] <= arr[m]:
            mini = min(mini, arr[l])
            l = m+1

        else:
            mini = min(mini, arr[m])
            h = m-1
    i=arr.index(mini)

    return i


arr=[4,5,6,7,0,1,2,3]
print(time_rotated(arr))
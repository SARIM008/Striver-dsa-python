def maxElement(arr, col):
    return max(range(len(arr)), key=lambda r: arr[r][col])


def peak2d(arr):
    n = len(arr)
    m = len(arr[0])

    l = 0
    h = m - 1

    while l <= h:

        mid = (l + h) // 2

        # row having maximum element in mid column
        mx = maxElement(arr, mid)

        # left neighbor
        left = arr[mx][mid - 1] if mid - 1 >= 0 else float('-inf')

        # right neighbor
        right = arr[mx][mid + 1] if mid + 1 < m else float('-inf')

        # current element
        curr = arr[mx][mid]

        # peak found
        if curr > left and curr > right:
            return [mx, mid]

        # move left
        elif left > curr:
            h = mid - 1

        # move right
        else:
            l = mid + 1

    return [-1, -1]

arr = [
      [4, 2, 5, 1, 4, 5],
      [2, 9, 3, 2, 3, 2],
      [1, 7, 6, 0, 1, 3],
      [3, 6, 2, 3, 7, 2]
  ]
print(peak2d(arr))
def single_non_duplicate(arr):
    n = len(arr)

    # Edge case: only one element
    if n == 1:
        return arr[0]

    # Check first element
    if arr[0] != arr[1]:
        return arr[0]

    # Check last element
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2

    while low <= high:

        mid = (low + high) // 2

        # Found unique element
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # mid belongs to left half (pairing valid)
        if ((mid % 2 == 1 and arr[mid] == arr[mid - 1]) or
            (mid % 2 == 0 and arr[mid] == arr[mid + 1])):

            low = mid + 1

        # pairing broken
        else:
            high = mid - 1


# Example
arr = [1,1,2,2,3,3,4,5,5]

print(single_non_duplicate(arr))
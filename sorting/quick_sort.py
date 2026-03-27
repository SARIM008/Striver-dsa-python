def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1

        while j >= low + 1 and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        pti = partition(arr, low, high)
        quicksort(arr, low, pti - 1)
        quicksort(arr, pti + 1, high)


# Driver code
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print(arr)
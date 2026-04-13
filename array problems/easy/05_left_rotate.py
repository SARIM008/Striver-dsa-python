def left(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
arr = [1, 2, 3, 4, 5]
print(left(arr))

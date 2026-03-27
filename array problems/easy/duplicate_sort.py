def duplicate(arr):
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            k=arr(i-1)
            arr.remove(k)
    return arr
arr=[1,1,2,2,2,3,3]
print(duplicate(arr))
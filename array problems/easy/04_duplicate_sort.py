def duplicate(arr):
    if not arr:
        return arr
    i=0
    for j in range(0,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1]
arr=[1,1,2,2,2,3,3]
print(duplicate(arr))
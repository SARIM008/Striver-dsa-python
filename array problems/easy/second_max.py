def s_max(arr):
    if len(arr)<2:
        return -1
    max1=arr[0]
    max2=float('-inf')
    for i in range(len(arr)):
        if max1<arr[i]:
            max2,max1=max1,arr[i]
        elif arr[i]>max2 and arr[i]!=max1:
            max2=arr[i]
    return max2
arr=[2,3,1,4,5,1444,13,789]
print(s_max(arr))

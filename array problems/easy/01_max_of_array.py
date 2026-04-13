def max(arr):
    m=arr[0]
    for i in range(len(arr)):
        if m<arr[i]:
            m=arr[i]
    print(m)
arr=[2,3,1,4,5,1444,13,789]
max(arr)

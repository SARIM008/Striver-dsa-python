def find(arr,t):
    n=len(arr)
    m=len(arr[0])
    i=0
    j=m-1
    while i<n and j>=0:
        if arr[i][j]==t:
            return i,j
        elif arr[i][j]<t:
            i+=1
        else:
            j-=1
    return "Not found"
arr = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
t=8
print(find(arr,t))
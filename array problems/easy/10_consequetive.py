def conn(arr):
    cnt=0
    mx=0
    for i in range(len(arr)):
        if arr[i]==1:
            cnt +=1
        else:
            cnt=0
        mx= max(mx,cnt)
    return mx

arr = [1, 1, 0, 1, 1, 1]
print(conn(arr))

def rotate_d(arr,t):
    l=0
    h=len(arr)-1
    while l<=h:
        m=(l+h)//2
        if arr[m]==t:
            return True
        elif arr[l]==arr[m] and arr[h]==arr[m]:
            l=l+1
            h=h-1
            continue
        elif arr[l]<=arr[m]:
            if t>=arr[l] and t<=arr[m]:
                h=m-1
            else:
                l=m+1
        elif arr[m]<=arr[h]:
            if arr[m]<=t and t<=arr[h]:
                l=m+1
            else:
                h=m-1
arr=[0,4, 5, 6, 7, 0, 1, 2,0]
t= 0
print(rotate_d(arr,t))
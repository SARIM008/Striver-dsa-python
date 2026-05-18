def lowerbound(arr,t):
    l=0
    h=len(arr)-1
    ans=len(arr)
    while l<h:
        mid=(l+h)//2
        if arr[mid]>=t:
            ans=mid
            h=mid-1
        elif arr[mid]<t:
            l=mid+1
    return ans
arr = [3, 5, 8, 15, 19]                # Sorted input array
t = 9
print(lowerbound(arr,t))   
    
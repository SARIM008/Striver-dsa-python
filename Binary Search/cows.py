def possible(arr,cows,d):
    count=1
    lp=0
    for i in range(1,len(arr)):
        if arr[i]-arr[lp]>=d:
            count+=1
            lp=i
        if count>=cows:
            return True
    return False

def optimal(arr,cows):
    arr.sort()
    l=0
    ans=float("-inf")
    h=arr[-1]-arr[0]
    while l<=h:
        mid=(l+h)//2
        if possible(arr,cows,mid):
            ans=max(mid,ans)
            l=mid+1
        else:
            h=mid-1
    return ans

arr = [0,3,4,7,10,9]
cows = 4
print(optimal(arr,cows))
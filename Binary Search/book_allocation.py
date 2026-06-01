def student_count(arr,page):
    student=1
    pagescount=0
    for i in range(len(arr)):
        if arr[i]+pagescount<=page:
            pagescount+=arr[i]
        else:
            student+=1
            pagescount=arr[i]
    return student
def optimal(arr,st):
    l=max(arr)
    h=sum(arr)
    ans=0
    while l<=h:
        mid=(l+h)//2
        if student_count(arr,mid)<=st:
            h=mid-1
            ans=mid
        else:
            l=mid+1
    return ans
arr = [12, 34, 67, 90]

st = 2
print(optimal(arr,st))
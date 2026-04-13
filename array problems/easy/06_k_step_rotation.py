def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def k_step(arr,side,k):
    n=len(arr)
    k=k%n
    if side.lower()=="right":
        reverse(arr,0,n-1)
        reverse(arr,0,k-1)
        reverse(arr,k,n-1)
        return arr
    if side.lower()=="left":
        reverse(arr,0,k-1)
        reverse(arr,k,n-1)
        reverse(arr,0,n-1)
        return arr
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
side = "right"
print(k_step(arr,side,k))


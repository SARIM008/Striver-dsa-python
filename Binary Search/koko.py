import math


def koko(arr,n):
    l=1
    h=max(arr)
    c=float('inf')
    while l<=h:
        t=0
        m=(l+h)//2
        for b in arr:
            t+=math.ceil(b/m)
        if t<=n:
            c=min(c,m)
            h=m-1
        elif t>n:
            l=m+1
    return c

arr = [3, 6, 7, 11]
n = 8
print(koko(arr,n))
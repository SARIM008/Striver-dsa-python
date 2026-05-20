def sqrt(a):
    l=1
    h=a
    c=0
    for i in range(1,a):
        m=(l+h)//2
        if (m**2)<=a:
            l=m+1
            c=m
        else:
            h=m-1
    return c
print(sqrt(37))


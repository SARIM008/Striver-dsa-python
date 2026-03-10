def decrease(n):
    if n==0:
        return
    print(n)
    decrease(n-1)
decrease(5)
def name(n,name):
    def helper(i):
        if i>n:
            return
        print(name)
        helper(i+1)
    helper(1)
name(5,"sarim")

def name2(i,n,name):
    if i>n:
        return
    i+=1
    print(name)
    name2(i,n,name)
name2(1,7,"yasir")
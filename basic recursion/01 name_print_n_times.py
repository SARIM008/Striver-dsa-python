def name(n,name):
    def helper(i):
        if i>n:
            return
        print(name)
        helper(i+1)
    helper(1)
name(5,"sarim")

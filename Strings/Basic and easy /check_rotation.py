def rotate(s,g):
    a=s+s
    if g in a:
        return True
    return False

s = "rotation"
g= "tionrota"
print(rotate(s,g))
def isomorphic(a,b):
    hmap1={}
    hmap2={}
    for c1,c2 in zip(a,b):
        if c1 in hmap1 and hmap1[c1]!=c2:
            return False
        if c2 in hmap2 and hmap2[c2]!=c1:
            return False
        hmap1[c1]=c2
        hmap2[c2]=c1
    return True
a="egg"
b="add"
print(isomorphic(a,b))
#!/usr/bin/env python
# coding: utf-8

# # 4 things to keep in mind
# 1) take row as outer loop
# 2) take column as inner loop 
# 3) always use print inside inner loop
# 4) observe symmetry and relation between outer and inner loop

# In[12]:


#first loop 
n=int(input("enter the size of pattern"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


# In[11]:


for i in range(5):
    print("* " * 5)


# pattern 2

# In[14]:


def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print()
pattern2(5)


# In[28]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    


# In[30]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# In[15]:


def pattern5(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
pattern5(5)


# In[37]:


n=int(input())
for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()


# In[10]:


def pattern7(n):
    
    for i in range(n):
        #to print spaces
        for j in range(n-i-1):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")

        print()
pattern7(5)


# In[11]:


def pattern8(n):
    
    for i in range(n):
        for k in range(i):
            print(" ",end=" ")
        for j in range(2*n-(2*i+1)):
            print("*",end=" ")
        for k in range(i):
            print(" ",end=" ")
        print()
pattern8(5)


# In[12]:


pattern7(5)
pattern8(5)


# In[17]:


pattern2(5)
pattern5(4)


# In[25]:


def pattern11(n):
    for i in range(n): #to set entry value
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(i+1):
            
            print(start,end="")
            #to loop between 0 and 1
            start=1-start
                
        print()
pattern11(5)


# In[65]:


def pattern12(n):
    space=2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for k in range(1,space+1):
            print(" ",end="")
        for f in range(i,0,-1):
            print(f,end="")
        print()
        space-=2
pattern12(4)


# In[72]:


def pattern13(n):
    start=1
    k=0
    for i in range(n+1):
        row=i
        for j in range(start,start+row):
            print(j,end=" ")
            k=j
        start=k+1
        print()
pattern13(6)
            


# In[74]:


chr(65)


# In[86]:


def pattern14(n):
    c=0
    for i in range(n+1):
        for j in range(0,i):
            print(chr(65+j),end="")
        print()
pattern14(5)


# In[101]:


def pattern15(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print(chr(65+j),end="")
        print()
pattern15(5)


# In[109]:


def pattern16(n):
    for i in range(n+1):
        for j in range(0,i):
            print(chr(64+i),end="")
        print()
pattern16(5)


# In[133]:


#palindrome pyramid
def pattern17(n):
    for i in range(n):
        k=65
        #spaces
        for j in range(n-i-1):
            print(" ",end=" ")
        #first increasing pyramid
        for j in range(i+1):
            print(chr(k+j),end=" ")
        #decreasing pyramid
        for j in range(i-1,-1,-1):
            print(chr(k+j),end=" ")
        print()
pattern17(5)


# In[153]:


def pattern18(n):
    for i in range(n):
        for j in range(n-1-i,n):
            print(chr(65+j),end=" ")
        print()
pattern18(5)


# In[194]:


def pattern19(n):
    s=0
    
    for i in range(n):
        s=2*i
        a=n-i
        print("*"*a,end="")
        print(" "*s,end="")
        print("*"*a,end="")
        s+=2
        print()
    k=0
    k=2*n-2
    for j in range(1,n+1):
        print("*"*j,end="")
        print(" "*k,end="")
        print("*"*j,end="")
        k-=2
        print()
    
pattern19(5)


# In[215]:


def pattern20(n):
    s=(2*n)
    print(s)
    for i in range(n+1):
        print("*"*i,end="")
        print(" "*s,end="")
        print("*"*i,end="")
        s-=2
        print()
    for i in range(n-1,0,-1):
        s=2*(n-1)-i-2
        print("*"*i,end="")
        print(" "*s,end="")
        print("*"*i,end="")
        print()
pattern20(5)


# In[222]:


def pattern21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
pattern21(6)


# In[ ]:





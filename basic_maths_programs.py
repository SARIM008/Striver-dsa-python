def digit_count(n):
    count=len(str(abs(n)))
    print(count)


import math
def digit_count_log(n):
    count=int(math.log10(n))+1
    return count

def num_reverse(n):
    num=0
    if n>0:
        sign=1
    if n<0:
        sign=-1
    while n>0:
        #taking out last digit 
        digit=n%10
        num=(num*10) +digit 
        n=n//10
    return num

def palindrome(n):
    if n==num_reverse(n):
        return("it is a palindrom")
    else:
        return("not a palindrome")


#Euclidean Algorithm: for finding GCD
#The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
#of two numbers. It operates on the principle that the GCD of two numbers remains
#the same even if the smaller number is subtracted from the larger number.
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def armstrong(n):
    #to get number of digits
    c=int(math.log10(n))+1
    b=0
    k=n
    while n>0:
        #getting each digit
        a=n%10
        b=b+(a**c)
        n=n//10
    if b==k:
        return "it is a armstrong number"
    else:
        return "not a armstrong number"

def divisor(n):
    l=[]
    #we will loop till square root only and store factors and then taking its pair and storing it
    for i in range(1,(int(math.sqrt(n))+1)):
        if n%i==0:
            l.append(i)
            if i!=n//i:
                l.append(n//i)
    l.sort()
    return l

def check_prime(n):
    c=0
    #checking if it has factors more 2 then not prime
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            c+=1
            if i!=n//i:
                c+=1
    if c>2:
        return "not a prime"
    else:
        return "it is prime"
print(check_prime(37))

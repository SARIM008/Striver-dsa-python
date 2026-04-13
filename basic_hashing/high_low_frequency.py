from collections import defaultdict

def high_low_freq(arr):
    df=defaultdict(int)
    max=0
    min=100000
    max_key=0
    min_key=0
    for i in arr:
        df[i]+=1
    
    for key,value in df.items():
        if value>max:
            max=value
            max_key=key
        if value<min:
            min=value
            min_key=key
    print(f"{max_key} has highest frequency which is {max}")
    print(f"{min_key} has lowest frequency which is {min}")
high_low_freq([10,5,10,15,10,5])

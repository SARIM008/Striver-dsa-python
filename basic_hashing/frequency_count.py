from collections import defaultdict
def frequency(arr):
    df=defaultdict(int)
    for i in arr:
        df[i]+=1
    for key,value in df.items():
        print(key,value)

frequency([10,5,10,15,10,5])

def insertion(arr):
    for i in range(len(arr)):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    print(arr)
insertion([10,100,20,25,3,96,5,4])
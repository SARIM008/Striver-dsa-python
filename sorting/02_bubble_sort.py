def bubble_Sort(arr):
    for i in range(len(arr)):
        swap=False
        #the range of for loop is like this because after swapping the 
        #largest will go at end and it will keep going in this manner
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        
        if not swap:
            break
    print(arr)
bubble_Sort([10,100,20,25,3,96,5,4])
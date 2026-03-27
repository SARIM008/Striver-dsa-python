def check_sort(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
    
arr=[1,2,6,4,5]
print(check_sort(arr))
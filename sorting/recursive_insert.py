def insert_sort(arr, i, n):
    
    if i == n:
        return
    j = i
    
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j -1]
        j -= 1
        
    insert_sort(arr,i + 1, n)
    


arr = [ 3,4,2,4,5]
n = len(arr)
i = 0
insert_sort(arr, i, n)
print(arr)
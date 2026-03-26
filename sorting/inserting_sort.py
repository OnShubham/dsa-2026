def inserting_arr(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        
        while j >=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return print(arr)


arr = [13, 46, 24, 52,1, 20, 9, 5]
inserting_arr(arr)
def bubble_sort(arr, n):
    
    if n == 1:
        return
    
    did_swap = False
    
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j] , arr[j + 1] = arr[j + 1], arr[j]
            did_swap = True
            
    
    if not did_swap:
        return
    
    bubble_sort(arr, n - 1)
    
    
arr = [22,2,1,2,3,4,5]
print(arr)
n = len(arr)
bubble_sort(arr,n)
print(arr)



def bubble_sort_1(arr, n):
    
    if n == 1:
        return
    
    did_swap = False
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            did_swap = True
            
            
    if not did_swap:
        return
        
        
    bubble_sort_1(arr, n - 1)
        
arr = [4,5,3,2]
n = len(arr)
print(arr)

bubble_sort_1(arr,n)
print(arr)
        
def largest_smallest(arr,n):
    
    if n < 2:
        return -1 , -1
    
    small = float('inf')
    secound_small = float('inf')
    largest = float('-inf')
    secound_largest = float('-inf')
    
    for i in range(n):
        
        small = min(small, arr[i])
        largest = max(largest, arr[i])
        
    for i in range(n):
        if arr[i] < secound_small and arr[i] != small:
            secound_small = arr[i]
        if arr[i] > secound_largest and arr[i] != largest:
            secound_largest = arr[i]
            
    print(secound_largest,"large")
    print(secound_small,"small")
    
    
if __name__ == "__main__":
    arr = [3,5,4,2,4,5,2,22,2,11,2,33,1,4,0]
    n = len(arr)
    largest_smallest(arr,n)
    
    
    
def largest_num(arr, n):
    
    if n < 2:
        return -1 -1 
    
    # small and large 
    
    small = float('inf')
    secound_small = float('inf')
    large = float('-inf')
    secound_large = float ('-inf')
    
    
    # find max and min
    
    
    for i in range(n):
        
        small = max(small,arr[i])
        large = min(large,arr[i])
        
        
    for i in range(n):
        if arr[i] < secound_small and arr[i] != small:
            secound_small = arr[i]
        if arr[i] > secound_large and arr[i] != large:
            secound_large = arr[i]
            
    print('small :', secound_small)
    print('large :', secound_large)
    

if __name__ == "__main__":
    arr = [1]
    n = len(arr)
    largest_num(arr, n)
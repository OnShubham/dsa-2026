def remove_duplicate(arr,n):
    
    if not arr:
        return 0
    
    i = 0
    
    for j in range(1, len(arr)):
        
        if arr[j] != arr[i]:
            
            i += 1
            
            arr[j] = arr[i]
            
    return i + 1
    


if __name__ == "__main__":
    arr = [2,3,1,2,3,4,4]
    n = len(arr)
    k = remove_duplicate(arr,n)
    print(arr[:k])
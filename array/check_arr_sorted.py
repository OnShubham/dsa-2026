def check_arr(arr,n):
    
    for i in range(n):
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                
                return print(False)
    return print(True)
    
    
    
    
def arr_1(arr,n):
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                return print(False)
    return print(True)
    


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    arr_1(arr,n)
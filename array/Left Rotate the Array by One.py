def left_rotate(arr,n):
    
    temp = arr[0]
    
    for i in range(1, n):
        
        arr [ i - 1] = arr[i]
        
        arr[-1] = temp
       
    
    
    
if __name__ == "__main__":
    
    arr = [2,3,4,5]
    n = len(arr)
    left_rotate(arr,n)
    print(arr)
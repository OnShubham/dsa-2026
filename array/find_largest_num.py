def find_large(arr, n):
    
    max = arr[0]# Initialize max with the first element in the array

    # Iterate through the array to find the maximum element
    for i in range(1, n):
        if arr[i] > max:  # If the current element is greater than max, update max
            max = arr[i]

    return max  # Return the largest element found


arr1 = [2, 5, 1, 3, 0]
n = len(arr1)  # Size of the array
max = find_large(arr1, n)  # Call the function to find the largest element
print("The largest element in the array is:", max)  



def find_large_num(num):
    
    max = num[0]
    
    for i in range(1, n):
        
        if arr[i] > max:
            max = arr[i]
            
    return max


def find_the_large_num(arr,n):
    
    max = arr[0]
    
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
            
            
    return print(max)

arr = [2,3,4,11,2,3,4]
n = len(arr)
find_the_large_num(arr,n)





def find_the_num(arr,n):
    
    max_value = arr[0]
    
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
            
    return print(max_value)

arr = [2,3,4,11,22,3,4]
n = len(arr)
find_the_num(arr,n)
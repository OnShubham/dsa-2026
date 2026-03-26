# def selection_sort(arr):
#     n = len(arr)
    
    
#     for i in range(n - 1):
#         min_index = i
        
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
                
        
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]
        
    
    
#     print(arr)
    
# arr = [13, 46, 24, 52, 20, 9]
# selection_sort(arr)



def sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        mini_index = i # assume small value here 
        
        for j in range(1, i + 1):
            if arr[j] <= arr[mini_index]:
                mini_index = j
                
        arr[i], arr[mini_index] = arr[mini_index], arr[i]
        

    return print(arr)

arr = [13, 46, 24, 52, 20, 9]
sort(arr)


def selection_sort(arr):
    
    length = len(arr)
    
    for i in range(length):
        mini_index = i
        
        for j in range(i + 1, length):
            
            if arr[j] < arr[mini_index]:
                mini_index = j
        
        
        arr[i], arr[mini_index] = arr[mini_index], arr[i]
    
    return print(arr)
arr = [13, 46, 24, 52, 20, 9]
selection_sort(arr)



def selection_sort_1(arr):
    
    lenght = len(arr)
    
    for i in range(lenght):
        min_index = i
        
        for j in range(i + 1, lenght):
            
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    
    return print(arr)
    


arr = [13, 46, 24, 52,1, 20, 9, 5]
selection_sort_1(arr)
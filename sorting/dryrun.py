def merge_sort(arr):
    
    # base case : if arr has 0 or 1 element it is already sorted 
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return merge(left_sorted, right_sorted)
    
    
def merge(left, right):
    merge = []
    i = j  = 0
    
    # compare elements from both elements
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    
    merge.extend(left[i:])
    merge.extend(right[j:])
    
    return merge

arr = [22,3,22,1,43,2,44,5]
sorted_arr = merge_sort(arr)

print("orignal", arr)
print("sorted", sorted_arr)


def sort_1(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    mid = len(arr) // 2 # divided arr in 2 parts 
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    
    left_sort = sort_1(left_arr)
    right_sort = sort_1(right_arr)
    
    return sort_2(left_sort, right_sort) # ✅ correct
    
    


def sort_2(left, right):
    
    sort = []
    
    i = j = 0
    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1
            
        
    sort.extend(left[i:])
    sort.extend(right[j:])
    
    return sort
    
    
arr = [22,3,22,1,43,2,44,5]
sorted_arr = sort_1(arr)

print("1",arr)
print("1", sorted_arr)



def sorted_num(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sort = sorted_num(left)
    right_sort = sorted_num(right)
    
    return sorted_num_2(left_sort, right_sort)


def sorted_num_2(left, right):
    
    merge = []
    
    i = j = 0
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
            
        
    merge.extend(left[i:])
    merge.extend(right[j:])
    
    return merge


arr = [2,4,5,4,3,1,2,3]
sorted_arr = sorted_num(arr)

print("latest :" , sorted_arr)
    
    

def test(arr):
    
    # check arr 
    
    if len(arr) <= 1:
        return arr
    
    # mid left right
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sort = test(left)
    right_sort = test(right)
    
    return test_1(left_sort, right_sort)
    
    
def test_1(left, right):
    
    empty = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            empty.append(left[i])
            i += 1
        else:
            empty.append(right[j])
            j += 1
            
    empty.extend(left[i:])
    empty.extend(right[j:])
    
    return empty
    

    
    
arr = [2,4,5,4,3,1,2,3]
sorted_arr = test(arr)

print("latest test:" , sorted_arr)
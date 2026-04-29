


arr = [2,3,4,1,3,6,2,1,2,3,4,1]

min_value = arr[0]
max_value = arr[0]

for num in arr:
    if num < max_value:
        max_value = num
    if num > min_value:
        min_value = num
        
print(min_value, max_value)
        





def max_min(arr):
    
    min_value = arr[0]
    max_value = arr[0]
    
    for num in arr:
        
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    print(min_value, max_value)


arr=[4,3,2,1,5,6,7,3,2] 
    
max_min(arr)






arr = [3,4,5,2,3,4,1]

max_vale = arr[0]
min_value = arr[0]

for num in arr:
    
    if num < max_vale:
        max_vale = num
    if num > min_value:
        min_value = num

print(max_vale,min_value)
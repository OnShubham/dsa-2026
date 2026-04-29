
def two_pointer(target,arr):
    
    for i in range(len(arr)):
        
        for j in range(i + 1, len(arr)):
            
            if arr[i] + arr[j] == target:
                return True
        
        
    return False




arr = [2,3,1,5,3]
target = 7

result = two_pointer(target,arr)
print(result)





def two_pointer_1(target,arr):
    
    
    l = len(arr)
    
    for i in range(l):
        
        for j in range(i + 1, l):
            
            if arr[i] + arr[j] == target:
                
                return True
    return False



arr = [2,3,1,5,3]
target = 7

result = two_pointer_1(target,arr)
print(result)

def calculatee(string):
    
    dict = {}
    
    for i in string:
        
        if dict[i] in 



string = "aassddssaa"
result = calculatee(string)
print(string)
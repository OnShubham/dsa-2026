def rever(n):
    
    #  Bruth Force Approch
    
    # arr = len(n)
    # temp = [0] * arr
    
    # for i in range(arr):
    #     temp[i] = n[arr - i - 1]
        
    
    # return temp
   



#  bruth approch

    # arr_lengh = len(n)
    # temp_value = [0] * arr_lengh
    
    # for i in range(arr_lengh):
        
    #     temp_value[i] = n[arr_lengh - i - 1]
        
        
    # return temp_value


# Better / Optimal Approach (Two Pointers — In Place)


    # start = 0
    # end = len(n) - 1
    
    # while start < end:
        
    #     # swap
    #     n[start], n[end] = n[end], n[start]
    #     # start the first >>>
    #     start += 1
    #     #  start the end first <<<<
    #     end -=1
        
    # return n
    
    
# two pointer QUestion

# 
    start = 0
    end = len(n) - 1
    
    while start < end:
        n[start], n[end] = n[end], n[start]
        start = +1
        end = -1
        
    return n
    
    

# n = [1,2,3,4,5]
# op = rever(n)
# print(op)

#  recirsive logics 
def recursive_reverse_arr(arr, start, end):
    
    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]
    
    recursive_reverse_arr(arr, start + 1, end - 1)


arr = [1,2,3,4,5]

recursive_reverse_arr(arr, 0, len(arr) - 1)

print(arr)



def recursive_logic(arr,start, end):
    
    
    #  check the number are not greater then
    if start >= end:
        return
    
    # swap
    
    arr[start], arr[end] = arr[end], arr[start]
    
    # logic 
    
    recursive_logic(arr, start + 1, end - 1)
    
    
    
    
arr = [1,2,3,4,5,2]

recursive_logic(arr,0, len(arr) -1 )

print(arr)


# two pointer

def two_pointer(n):
    
    start = 0 
    end = len(n) - 1
    
    while start < end:
        n[start], n[end] = n[end], n[start]
        
        start = + 1
        end = - 1
        
    return n
    
    
    
n = [1,2,3,2,3,4]
ans = two_pointer(n)
print(ans)


def recursive_2(arr, start,end):
    
    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]
    
    recursive_2(arr, start + 1, end - 1)
    return arr
    
    
arr = [8,6,5,4,3,2,1]
recursive_2(arr, 0,len(arr) - 1)
print(arr)
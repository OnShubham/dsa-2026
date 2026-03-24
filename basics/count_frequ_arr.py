def count_freq_arr(arr):
    # store repeated
    freq = {}
    # loops
    for num in arr:
        
        # check again the number and store
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    # return print(freq)

    for num, count in freq.items():
        
        if count > 1:
             print(num, count)
    
    

arr = [10,5,10,15,10,5]
count_freq_arr(arr)
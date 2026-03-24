def hashing_arr_duplicaet(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    
    
    # print(freq)
    # shortlist a number 1 > 
    for num, count in freq.items():
        if count > 1:
            print(num,count)




arr = [1, 2, 2, 3, 1, 4,4]
hashing_arr_duplicaet(arr)
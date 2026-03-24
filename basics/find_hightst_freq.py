def high_freq(arr):
    
    freq = {}
    
    for num in arr:
        
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    print(freq)
    
    for num, count in freq.items():
        if num > 1:
            print(num,count)
        
    
    
arr = [2,3,4,2,2,3,3,4,5,2]
high_freq(arr)
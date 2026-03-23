def find_repeated_char(s):
    
    freq = {}
    
    for ch in s:
        
        if ch in freq:
            freq[ch] += 1
        
        else:
            freq[ch] = 1
            
    for ch, count in freq.items():
        if count > 1:
            print(ch,count)
            
find_repeated_char("datascrience")


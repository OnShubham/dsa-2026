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
            
# find_repeated_char("datascrience")



def find_the_reapeted(n):
    
    disc = {}
    
    for char in n:
        
        if char in disc:
            disc[char] += 1
        
        else:
            disc[char] = 1
            
    for char, count in disc.items():
        if count > 1:
            print(char, count)
            
find_the_reapeted("datascrience")
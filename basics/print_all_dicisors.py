def all_devisore(n):
    
    res = []
    
    for i in range(1,n + 1):
        
        if n % i == 0:
            
            res.append(i)
            
    
    return res


n = 36
print(all_devisore(n))



def armstrong_2(n):
    
    num = []
    
    for i in range(1, n + 1):
        
        if n % i == 0 :
            
            num.append(i)
            
    return num


n = 36
print(armstrong_2(n))
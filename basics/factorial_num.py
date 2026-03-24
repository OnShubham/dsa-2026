def fact(n):
    fact = 1
    
    for i in range(1, n + 1):
        
        fact *= i 
        
    
    return print(fact)
        
        
    
    
n = 10
fact(n)



def rec_fact(n):
    
    if n == 0:
        
        return 1
    
    # recursive logic
    return n * rec_fact(n - 1)

n = 10
print(rec_fact(n))
def prime_num(n):
    
    cnt = 0
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            cnt += 1
            
        
    return cnt == 2


           
n = 2
isprime = prime_num(n)

if isprime:
    print(f"{n} is a prime number")
else:print(f"{n} is not a prime number.")
    



def secound(n):
    
    cnt = 0
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            cnt += 1
            
    return cnt == 2

           
n = 5
isprime = secound(n)

if isprime:
    print(f"{n} is a prime number")
else:print(f"{n} is not a prime number.")
    
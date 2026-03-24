def armstrong(num):
    
    k = len(str(num))
    sum = 0
    n = num
    while n > 0:
        id = n % 10
        sum += id ** k
        n = n // 10
        
    return sum == num  
    
num = 153

if armstrong(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} not armstrong")
    

def arm_1(num):
    
    k = len(str(num))
    sum = 0
    n = num 
    
    while n > 0:
        
        id = n % 10
        sum += id ** k 
        n = n // 10
        
    return sum == num

    
num = 153

if arm_1(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} not armstrong")
# print(armstrong(num))
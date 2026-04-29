

n = int(input("enter the number"))

rev = 0

while n != 0:
    
    digits = n % 10
    
    rev = rev * 10 + digits
    
    n = n // 10
print(rev)




num = int(input("  "))

rev = 0

while num != 0:
    digits = num % 10
    
    rev = rev * 10 + digits
    
    num = num // 10
    
print(rev)
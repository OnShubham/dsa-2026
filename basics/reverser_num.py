

def reverse_num(n):
    
    rever_num = 0
    
    while n > 0:
        
        # get the last digits
        lastdigits = n % 10
        
        # Append in the reversnumenre
        
        rever_num = rever_num * 10 + lastdigits
        
        
        # remove the last digis from n 
        n = n // 10
        
    return rever_num


if __name__ == "__main__":
    n = 5687
    print("N:", n)
    digits = reverse_num(n)
    print("Number of Digits in N:", digits)
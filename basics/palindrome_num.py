def palindrome(n):
    
    check = n
    
    revNum = 0
    
    while n > 0:
        
        
        lastdigits = n % 10
        
        revNum = revNum * 10 + lastdigits
        
        n = n // 10
        
        
    if revNum == check :
        return print("palindrome Num", revNum)
    else:
        return print("not palindrome num", revNum)


if __name__ == "__main__":
    n = 1558879
    print("N:", n)
    digits = palindrome(n)
    # print("Number of Digits in N:", digits)
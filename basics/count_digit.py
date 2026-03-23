
def countDigits(n):
    
    # init a counter varibale
    # cnt store a counter of digis 
    cnt = 0
    
    while n > 0:
        
        
        
        cnt = cnt + 1
        
        # divised n  by 10
        # remove the last digis
        n = n // 10
        
    return cnt



if __name__ == "__main__":
    N = 5687
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)
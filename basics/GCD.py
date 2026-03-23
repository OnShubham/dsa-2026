# Greatest common devisor 

def findGcd(n1, n2):
    
    for i in range(min(n1,n2), 0, -1):
        
        if n1 % i == 0 and n2 % i == 0:
            
            return i
        
        
    return 1

def main():
    
    n1 = 8
    n2 = 15
    
    gcd = findGcd(n1, n2)
    
    print("GCD of", n1, "and", n2, "is:", gcd)


if __name__ == "__main__":
    main()
    
def is_prime(x):
    i=2
    if x < 2:
        return False
    else:    
        while i <= x :
            if x % i ==0 and x == i:
                return True
            elif x % i ==0 :
                return False
            else:
                i += 1
    

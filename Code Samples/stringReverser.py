def reverse(text):
    n=''
    x  = len(text)
    while (x>0):
        n += text[x-1]
        x += -1
    print n
    return n
    

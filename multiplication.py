def multiply(a,b):
    if b == 0:
        return 0  

    if b < 0:
        return -a + multiply(a,b+1)
    
    if b > 0:
        return a + multiply(a,b-1)


print(multiply(-3,-3))
#(m,n) if m == 0  = n+1
# if m>0 and n==0 : A(m-1,1)
# if m>0 and n>0 : A(m-1,A(m,n-1))

def ackerman(m,n):
    if m == 0:
        n += 1
        return n

    if m > 0 and n == 0:
        return ackerman(m-1,1)

    if m > 0 and n > 0: 
        return ackerman(m-1,ackerman(m,n-1))

print(ackerman(3,0))

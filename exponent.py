#O(n) linear time in value of exp


def power(base,exp):    
    if exp == 0:
        return 1

    return base * power(base, exp -1)

print(power(4,4))
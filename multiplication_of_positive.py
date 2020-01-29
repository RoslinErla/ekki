# O(n)  linear time in value of multiplier

def multiply_positiive(base,multiplier):
    ret_val = 0
    for _ in range(multiplier):
        ret_val = ret_val + base
    return ret_val

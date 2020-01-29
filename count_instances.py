# ● Count instances
# ○ Implement a recursive function that counts a specific value in a list
# ○ Takes a list and a single value as parameters
# ○ Returns an integer value
# ■ How many times does that value appear in the list?

def count(a_list,value):
    if a_list == []:
        return 0
    
    if value ==  a_list[-1]:
        return 1 + count(a_list[:-1],value)
    else:
        return count(a_list[:-1],value)

print(count(["m","a","m","m","a","m"],"m"))

# Are there duplicates in a list?
# ○ Implement a recursive function that checks for duplicate values in a list
# ○ Takes a list as a parameter
# ○ Returns a boolean value
# ■ True if any value in the list appears more than once, otherwise False

def duplicates(a_list):
    if a_list == []:
        return False
    if a_list[-1] in a_list[:-1]:
        return True
    else: 
        duplicates(a_list[:-1])

duplicates(["m","a"])



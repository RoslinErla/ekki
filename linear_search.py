# ● Linear search
# ○ Implement a recursive function that searches for a value in a list
# ○ Takes a list and a single value as parameters
# ○ Returns a boolean value
# ■ True if the value is in the list, otherwise False

def linear_search(a_list,value):
    if a_list == []:
        return False

    if value == a_list[-1]:
        return True
    else:
        return linear_search(a_list[:-1],value)

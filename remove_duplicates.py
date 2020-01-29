# ● Remove duplicates
# ○ Implement a recursive function that removes duplicate values in a list
# ○ Takes a list as a parameter
# ○ Returns another list
# ■ List with all the same values, but only one instance of each value

def remove_duplicates(a_list, new_list = []):
    if a_list == []:
        return new_list

    if a_list[-1] in new_list:
        return remove_duplicates(a_list[:-1],new_list)
    else:
        new_list.append(a_list[-1])
        return remove_duplicates(a_list[:-1],new_list)

a_list = ["m","a","m","m","a","p"]

print(remove_duplicates(a_list))
        
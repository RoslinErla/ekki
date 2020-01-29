def is_substring(substring,a_str):
    """Is the string substring actually a substring in a_str"""
    if len(substring) > len(a_str):
        return False

    if len(substring) == len(a_str):
        if substring == a_str:
            return True
        else:
            return False

    if a_str[:len(substring)]== substring:
        return True

    else: 
        return is_substring(substring,a_str[1:])


print(is_substring("gnesk","gagnaskipan"))
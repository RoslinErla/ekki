# ● Length of string
# ○ Implement a recursive function that calculates the length of a string
# ○ Takes a string as a parameter
# ○ Returns an integer (+1 for each character)
# Note that you can use built in syntax for a string exactly as if it were a list where each
# item is a character. “abcd”[2] == ‘c’ ... “abcd”[:-1] == “abc” ... “abcd”[1:] == “bcd”


def len_of_str(string):
    if len(string) == 0:
        return 0

    return 1 + len_of_str(string[:-1])
    

print(len_of_str("Mamman"))
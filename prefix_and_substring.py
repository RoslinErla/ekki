def is_prefix(prefix,a_str):
    if len(prefix) == 0:
        return True
    if len(a_str) == 0:
        return False
    if prefix[0] != a_str[0]:
        return False
    return is_prefix(prefix[1:],a_str[1:])


def is_substring(sub,a_str):
    if len(a_str) == 0:
        if len(sub) == 0:
            return True
        else:
            return False
    if is_prefix(sub, a_str):
        return True
    return is_substring(sub,a_str[1:])

print(is_substring("gnask", "gagnaskipan"))
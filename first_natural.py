def first_n(n):
    if n == 0:
        return n
    first_n(n-1)
    print(n, end = " ")

first_n(6)
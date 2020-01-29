def fibonacci(x, num1 = 0, num2 = 1):

    if x == 0:
        return num1

    next_num = num2
    num2 = num1 + num2
    return fibonacci(x-1,next_num,num2)


print(fibonacci(10))
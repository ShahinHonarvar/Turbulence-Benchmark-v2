def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_95 = fib(95)
    return decimal_number % fib_95 == 0
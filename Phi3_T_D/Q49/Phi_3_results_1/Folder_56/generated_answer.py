def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(bin_str):
    decimal_number = int(bin_str, 2)
    fib_number = fib(83)
    return decimal_number % fib_number == 0
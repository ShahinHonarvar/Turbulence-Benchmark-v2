def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(bin_str):
    decimal_val = int(bin_str, 2)
    fib_34 = fib(34)
    return decimal_val % fib_34 == 0
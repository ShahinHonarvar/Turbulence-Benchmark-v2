def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def from_binary(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_num = from_binary(binary_str)
    fib_179 = fib(179)
    return decimal_num % fib_179 == 0
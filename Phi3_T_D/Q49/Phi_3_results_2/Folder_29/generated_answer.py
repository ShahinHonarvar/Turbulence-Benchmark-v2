def bin_to_dec(binary_str):
    return int(binary_str, 2)

def fib_number(n):
    if n in {0, 1}:
        return n
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_str):
    aim_fib_num = fib_number(117)
    decimal_num = bin_to_dec(binary_str)
    return decimal_num % aim_fib_num == 0
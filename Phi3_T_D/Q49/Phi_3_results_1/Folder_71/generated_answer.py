def fib_mod_147(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, (a + b) % 147)
    return a

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_mod_147(147) == 0
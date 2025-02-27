def fib_at(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def fib_17():
    return fib_at(17)

def if_decimal_is_divisible(binary_str):
    num_decimal = binary_to_decimal(binary_str)
    return num_decimal % fib_17() == 0
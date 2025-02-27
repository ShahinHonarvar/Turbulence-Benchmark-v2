def fib_67():
    a, b = (0, 1)
    for _ in range(66):
        a, b = (b, a + b)
    return a

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_67() == 0
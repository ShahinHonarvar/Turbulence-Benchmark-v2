def bin_to_decimal(binary_str):
    return int(binary_str, 2)

def get_nth_fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = bin_to_decimal(binary_str)
    fib_139th = get_nth_fibonacci(139)
    return decimal % fib_139th == 0
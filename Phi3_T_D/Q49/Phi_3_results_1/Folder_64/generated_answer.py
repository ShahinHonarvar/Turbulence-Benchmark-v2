def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    if decimal_value % fibonacci(9) == 0:
        return True
    else:
        return False
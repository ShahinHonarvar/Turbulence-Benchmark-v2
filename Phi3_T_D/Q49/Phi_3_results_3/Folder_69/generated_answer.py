def if_decimal_is_divisible(binary_string):
    fib_170 = _calculate_fib_170th()
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_170 == 0

def _calculate_fib_170th():
    a, b = (0, 1)
    for _ in range(169):
        a, b = (b, a + b)
    return a
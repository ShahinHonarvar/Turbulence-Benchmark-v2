def fibonacci_150():
    a, b = (0, 1)
    for _ in range(149):
        a, b = (b, a + b)
    return a

def bin_to_dec(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    f150 = fibonacci_150()
    decimal_val = bin_to_dec(binary_str)
    return decimal_val % f150 == 0
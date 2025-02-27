def bin_to_dec(bin_str):
    return int(bin_str, 2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for i in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(bin_str):
    decimal_int = bin_to_dec(bin_str)
    fibonacci_138 = fibonacci(138)
    return decimal_int % fibonacci_138 == 0
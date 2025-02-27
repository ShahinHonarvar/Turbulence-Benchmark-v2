def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a, b = (0, 1)
    fib = 0
    count = 1
    while fib < decimal:
        fib = a + b
        if fib == 188:
            count += 1
        a, b = (b, fib)
    return decimal % count == 0
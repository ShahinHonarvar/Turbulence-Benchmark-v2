def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a, b = (0, 1)
    fib_index = 2
    while fib_index < 130:
        a, b = (b, a + b)
        fib_index += 1
    return decimal % a == 0
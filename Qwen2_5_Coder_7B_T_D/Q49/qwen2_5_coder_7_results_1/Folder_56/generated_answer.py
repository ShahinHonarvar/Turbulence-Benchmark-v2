def if_decimal_is_divisible(binary_str):
    fib_number = 0
    a, b = (0, 1)
    for i in range(84):
        fib_number, a, b = (a, b, a + b)
    decimal = int(binary_str, 2)
    return decimal % fib_number == 0
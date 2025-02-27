def if_decimal_is_divisible(binary_str):
    n = 0
    a, b = (0, 1)
    counter = 1
    while counter < 107:
        a, b = (b, a + b)
        counter += 1
    target_fib_number = a
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fib_number == 0
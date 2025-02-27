def if_decimal_is_divisible(binary_str):
    fibonacci_number = 0
    a, b = (0, 1)
    for i in range(160):
        fibonacci_number = a
        a, b = (b, a + b)
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_number == 0
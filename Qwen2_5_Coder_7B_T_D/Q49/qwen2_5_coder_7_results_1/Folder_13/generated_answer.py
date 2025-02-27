def if_decimal_is_divisible(binary_str):
    fibonacci_number = 174
    a, b = (0, 1)
    while fibonacci_number > 0:
        a, b = (b, a + b)
        fibonacci_number -= 1
    decimal_number = int(binary_str, 2)
    return decimal_number % b == 0
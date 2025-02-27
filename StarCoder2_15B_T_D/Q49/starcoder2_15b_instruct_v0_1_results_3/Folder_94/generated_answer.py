def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = fib(40)
    return decimal_integer % fibonacci_number == 0
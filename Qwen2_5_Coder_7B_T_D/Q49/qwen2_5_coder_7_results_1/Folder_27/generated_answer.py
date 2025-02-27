def if_decimal_is_divisible(binary_str):
    fibonacci_87 = 44723316189700376520687668379044557034504
    decimal = int(binary_str, 2)
    return decimal % fibonacci_87 == 0
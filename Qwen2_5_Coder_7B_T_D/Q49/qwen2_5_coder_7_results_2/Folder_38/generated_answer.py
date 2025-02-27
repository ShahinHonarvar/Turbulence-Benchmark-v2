def if_decimal_is_divisible(binary_str):
    fibonacci_78 = 25578048657905210757813988749894873203833
    decimal = int(binary_str, 2)
    return decimal % fibonacci_78 == 0
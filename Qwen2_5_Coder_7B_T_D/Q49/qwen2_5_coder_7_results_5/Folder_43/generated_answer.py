def if_decimal_is_divisible(binary_str):
    fib_77 = 12586269025
    decimal = int(binary_str, 2)
    return decimal % fib_77 == 0
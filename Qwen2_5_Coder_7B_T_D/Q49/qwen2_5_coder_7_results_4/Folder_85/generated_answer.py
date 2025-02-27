def if_decimal_is_divisible(binary_str):
    fib_45 = 1134903170
    decimal = int(binary_str, 2)
    return decimal % fib_45 == 0
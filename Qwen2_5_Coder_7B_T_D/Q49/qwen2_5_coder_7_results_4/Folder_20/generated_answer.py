def if_decimal_is_divisible(binary_str):
    fib_100 = 354224848179261915075
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_100 == 0
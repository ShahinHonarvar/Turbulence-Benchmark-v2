def if_decimal_is_divisible(binary_str):
    fib_179 = 354224848179261915075
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_179 == 0
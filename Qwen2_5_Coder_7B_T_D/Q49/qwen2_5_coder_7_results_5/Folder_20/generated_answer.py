def if_decimal_is_divisible(binary_str):
    fib_100 = 354224848179261915075
    decimal = int(binary_str, 2)
    return decimal % fib_100 == 0
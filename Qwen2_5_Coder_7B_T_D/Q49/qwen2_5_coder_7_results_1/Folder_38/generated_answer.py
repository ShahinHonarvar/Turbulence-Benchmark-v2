def if_decimal_is_divisible(binary_str):
    fib_78 = 2497445781229890625
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_78 == 0
def if_decimal_is_divisible(binary_str):
    fib_1_2584 = 10946
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_1_2584 == 0
def if_decimal_is_divisible(binary_str):
    fib_159 = 2584412254719091126352690058845599124223
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_159 == 0
def if_decimal_is_divisible(binary_str):
    fib_66 = 17167680177565
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_66 == 0
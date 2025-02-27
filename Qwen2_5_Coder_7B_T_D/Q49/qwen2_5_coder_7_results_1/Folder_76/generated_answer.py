def if_decimal_is_divisible(binary_str):
    fib_188 = 25974847717432704406437556079130780264157273730656
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_188 == 0
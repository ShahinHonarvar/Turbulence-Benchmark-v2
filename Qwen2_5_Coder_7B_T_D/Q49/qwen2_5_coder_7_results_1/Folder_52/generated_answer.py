def if_decimal_is_divisible(binary_str):
    fib_176 = 25844117660233037603166258242812904496
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_176 == 0
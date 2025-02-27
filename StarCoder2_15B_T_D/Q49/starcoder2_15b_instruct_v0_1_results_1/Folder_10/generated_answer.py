def if_decimal_is_divisible(binary_rep):
    decimal_int = int(binary_rep, 2)
    first_88_fib_number = 24157817
    return decimal_int % first_88_fib_number == 0
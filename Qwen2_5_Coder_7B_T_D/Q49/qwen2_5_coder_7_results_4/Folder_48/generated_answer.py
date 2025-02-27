def if_decimal_is_divisible(binary_str):
    fib_198 = 14962455074623856385911756247757159795716428759157826327080
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_198 == 0
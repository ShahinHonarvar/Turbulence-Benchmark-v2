def if_decimal_is_divisible(binary_str):
    fib_150 = 12586269025
    decimal_num = sum((int(bit) * 2 ** idx for idx, bit in enumerate(reversed(binary_str))))
    return decimal_num % fib_150 == 0
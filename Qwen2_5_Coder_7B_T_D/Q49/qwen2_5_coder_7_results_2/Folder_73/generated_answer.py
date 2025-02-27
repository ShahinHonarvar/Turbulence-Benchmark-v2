def if_decimal_is_divisible(binary_str):
    fib_164 = 4346655761317812911134324485399494437
    decimal = int(binary_str, 2)
    return decimal % fib_164 == 0
def if_decimal_is_divisible(binary_str):
    fib_105 = 1447233402467622129175257412673
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_105 == 0
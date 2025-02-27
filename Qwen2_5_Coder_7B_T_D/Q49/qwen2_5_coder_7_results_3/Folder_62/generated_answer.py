def if_decimal_is_divisible(binary_str):
    fib_130 = 258441755413834326310414700758353296148222862010986568542494923801952000565592717
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_130 == 0
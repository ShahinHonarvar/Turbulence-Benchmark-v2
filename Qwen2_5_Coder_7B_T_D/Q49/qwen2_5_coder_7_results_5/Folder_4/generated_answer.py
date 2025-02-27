def if_decimal_is_divisible(binary_str):
    fib_118 = 259641934586269751609850504196021315884197779281587214175398719440502995605375
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_118 == 0
def if_decimal_is_divisible(binary_str):
    index_74 = 74
    fibonacci_74 = round(1 / sqrt(5) * (pow((1 + sqrt(5)) / 2, index_74) - pow((1 - sqrt(5)) / 2, index_74)))
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_74 == 0
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1, 1, 2, 3, 5, 8]
    decimal = int(binary_str, 2)
    return decimal % fibonacci[5] == 0
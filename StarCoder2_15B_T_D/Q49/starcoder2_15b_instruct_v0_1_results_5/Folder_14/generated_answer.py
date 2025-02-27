def binary_to_decimal(binary_string):
    decimal_int = 0
    for i, bit in enumerate(binary_string[::-1]):
        decimal_int += int(bit) * 2 ** i
    return decimal_int

def if_decimal_is_divisible(binary_string):
    decimal_int = binary_to_decimal(binary_string)
    a, b = (0, 1)
    for _ in range(27):
        a, b = (b, a + b)
    return decimal_int % b == 0
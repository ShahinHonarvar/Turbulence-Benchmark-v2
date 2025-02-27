def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def if_decimal_is_divisible(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    fib_num = next((x for i, x in enumerate(fib()) if i == 59))
    return decimal_num % fib_num == 0
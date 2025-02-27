def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 7:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divisor = fibonacci[6]
    decimal_value = int(binary_str, 2)
    return decimal_value % divisor == 0
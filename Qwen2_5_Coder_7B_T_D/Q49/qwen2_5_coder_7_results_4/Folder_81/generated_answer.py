def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(95):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divisor = fibonacci[97]
    decimal = int(binary_str, 2)
    return decimal % divisor == 0
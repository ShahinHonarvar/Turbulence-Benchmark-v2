def if_decimal_is_divisible(binary_str):
    fibonacci_number = [0, 1]
    while len(fibonacci_number) <= 38:
        fibonacci_number.append(fibonacci_number[-1] + fibonacci_number[-2])
    decimal = int(binary_str, 2)
    return decimal % fibonacci_number[38] == 0
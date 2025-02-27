def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 144):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return decimal_int % fibonacci_numbers[143] == 0
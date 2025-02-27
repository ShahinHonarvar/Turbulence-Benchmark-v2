def if_decimal_is_divisible(binary_string: str) -> bool:
    decimal_int = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 11):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return decimal_int % fibonacci_numbers[9] == 0
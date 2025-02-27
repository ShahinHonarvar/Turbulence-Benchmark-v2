def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    for i in range(2, 139):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_numbers[138] == 0
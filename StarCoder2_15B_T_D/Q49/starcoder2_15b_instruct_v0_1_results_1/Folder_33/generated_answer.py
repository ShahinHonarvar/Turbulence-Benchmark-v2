def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, base=2)
    fibonacci_numbers = [0, 1]
    for _ in range(133):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_int % fibonacci_numbers[134] == 0
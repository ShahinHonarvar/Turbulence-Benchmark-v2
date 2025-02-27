def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 110):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    if decimal_integer % fibonacci_numbers[109] == 0:
        return True
    else:
        return False
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    first_24_fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
    if decimal_integer % first_24_fibonacci_numbers[23] == 0:
        return True
    else:
        return False
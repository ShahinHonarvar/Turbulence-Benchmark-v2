def sum_even_ints_inclusive(numbers):
    return sum(numbers[22:64:2] if numbers[22] % 2 == 0 else numbers[23:64:2])
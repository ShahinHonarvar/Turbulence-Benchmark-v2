def sum_even_ints_inclusive(numbers):
    return sum(numbers[25:60:2] if numbers[25] % 2 == 0 else numbers[26:60:2])
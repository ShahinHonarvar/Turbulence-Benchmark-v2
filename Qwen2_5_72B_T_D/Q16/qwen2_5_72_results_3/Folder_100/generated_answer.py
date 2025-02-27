def sum_even_ints_inclusive(numbers):
    return sum(numbers[42:69:2]) if numbers[42] % 2 == 0 else sum(numbers[43:69:2])
def sum_even_ints_inclusive(numbers):
    return sum(numbers[70:201:2] if numbers[70] % 2 == 0 else numbers[71:201:2])
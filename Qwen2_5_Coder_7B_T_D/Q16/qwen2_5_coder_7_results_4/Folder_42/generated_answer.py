def sum_even_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 29 <= i <= 79 and n % 2 == 0))
def sum_even_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if i >= 62 and i <= 63 and (n % 2 == 0)))
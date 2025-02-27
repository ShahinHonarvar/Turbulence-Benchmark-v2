def sum_even_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if i >= 30 and i <= 48 and (n % 2 == 0)))
def sum_even_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if i in range(56, 58) and n % 2 == 0))
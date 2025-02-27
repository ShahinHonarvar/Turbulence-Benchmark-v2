def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 42 <= i <= 68 and n % 2 != 0)) if len(numbers) > 68 else 0
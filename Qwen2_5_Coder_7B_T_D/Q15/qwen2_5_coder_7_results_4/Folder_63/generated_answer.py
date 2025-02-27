def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 22 <= i <= 88 and n % 2 != 0))
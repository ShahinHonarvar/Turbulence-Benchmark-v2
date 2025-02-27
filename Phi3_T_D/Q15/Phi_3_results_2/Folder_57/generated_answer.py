def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 27 <= i <= 55 and n % 2 != 0)) or 0
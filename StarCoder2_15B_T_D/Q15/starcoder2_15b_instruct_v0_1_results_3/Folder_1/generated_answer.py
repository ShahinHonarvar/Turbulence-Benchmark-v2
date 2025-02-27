def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 31 <= i <= 72 and n % 2 == 1))
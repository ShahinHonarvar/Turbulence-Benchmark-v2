def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if i >= 22 and i <= 63 and (n % 2 != 0)))